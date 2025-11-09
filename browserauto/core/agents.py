"""Agent configuration and initialization"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm
from dotenv import load_dotenv
import os

from .tools import (
    see_screen,        # Vision tool - see what's on screen
    perform_action,    # Action tool - execute tasks
    move_mouse,        # Mouse movement
    click_mouse,       # Mouse clicking
    get_mouse_position # Mouse position info
)
from .prompts import (
    COORDINATOR_PROMPT,
    TASK_PLANNER_PROMPT,
    EXECUTOR_PROMPT,
    REPORTER_PROMPT
)

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Higher free tier: 1500 requests/day 
    google_api_key=api_key,
    convert_system_message_to_human=True
)

# ============================================================================
# AGENT DEFINITIONS
# ============================================================================

# 1. COORDINATOR - Receives user requests and orchestrates workflow
coordinator = create_react_agent(
    model,
    [
        create_handoff_tool(
            agent_name="TaskPlanner",
            description="Transfer to TaskPlanner to create detailed execution plan for the user's request"
        ),
        create_handoff_tool(
            agent_name="Reporter",
            description="Transfer to Reporter to get final results and summary"
        )
    ],
    prompt=COORDINATOR_PROMPT,
    name="Coordinator",
)

# 2. TASK PLANNER - Creates detailed step-by-step execution plans
task_planner = create_react_agent(
    model,
    [
        create_handoff_tool(
            agent_name="Executor",
            description="Transfer to Executor to execute the planned tasks"
        ),
        create_handoff_tool(
            agent_name="Coordinator",
            description="Transfer back to Coordinator if clarification needed"
        )
    ],
    prompt=TASK_PLANNER_PROMPT,
    name="TaskPlanner",
)

# 3. EXECUTOR - Executes the computer automation tasks
executor = create_react_agent(
    model,
    [
        # Primary tools - Vision and Action
        see_screen,           # SEE what's on screen
        perform_action,       # ACT based on what was seen
        
        # Mouse control tools
        move_mouse,
        click_mouse,
        get_mouse_position,
        
        # Handoff tools
        create_handoff_tool(
            agent_name="Reporter",
            description="Transfer to Reporter when execution is complete to format results"
        ),
        create_handoff_tool(
            agent_name="TaskPlanner",
            description="Transfer back to TaskPlanner if plan needs adjustment or step failed"
        )
    ],
    prompt=EXECUTOR_PROMPT,
    name="Executor",
)

# 4. REPORTER - Formats and reports results back to user
reporter = create_react_agent(
    model,
    [
        see_screen,
        get_mouse_position,
        create_handoff_tool(
            agent_name="Coordinator",
            description="Transfer back to Coordinator with final report"
        )
    ],
    prompt=REPORTER_PROMPT,
    name="Reporter",
)

# ============================================================================
# SWARM CREATION
# ============================================================================

# Create the swarm workflow with all agents
checkpointer = InMemorySaver()
workflow = create_swarm(
    [coordinator, task_planner, executor, reporter],
    default_active_agent="Coordinator"  # Start with Coordinator
)

# Compile the workflow
swarm_app = workflow.compile(checkpointer=checkpointer)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_swarm_response(message: str, thread_id: str = "default"):
    """
    Get a response from the swarm agents
    
    Workflow:
    1. User message → Coordinator
    2. Coordinator → TaskPlanner (with TODO list)
    3. TaskPlanner → Executor (with detailed steps)
    4. Executor executes using computer_control
    5. Executor → Reporter (with results)
    6. Reporter → Coordinator (with formatted report)
    7. Coordinator → User (final response)
    
    Args:
        message: The user's message
        thread_id: Unique identifier for the conversation thread
    
    Returns:
        dict: The response from the agents including all handoffs
    """
    config = {"configurable": {"thread_id": thread_id}}
    response = swarm_app.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config,
    )
    return response


def stream_swarm_response(message: str, thread_id: str = "default"):
    """
    Stream responses from the swarm agents in real-time
    
    This allows you to see each agent's work as it happens:
    - Coordinator analyzing request
    - TaskPlanner creating steps
    - Executor performing actions
    - Reporter formatting results
    
    Args:
        message: The user's message
        thread_id: Unique identifier for the conversation thread
    
    Yields:
        dict: Streaming chunks of agent responses
    """
    config = {"configurable": {"thread_id": thread_id}}
    for chunk in swarm_app.stream(
        {"messages": [{"role": "user", "content": message}]},
        config,
        stream_mode="updates"
    ):
        yield chunk


def get_conversation_history(thread_id: str = "default"):
    """
    Get the conversation history for a specific thread
    
    Args:
        thread_id: The conversation thread ID
    
    Returns:
        list: List of messages in the conversation
    """
    config = {"configurable": {"thread_id": thread_id}}
    state = swarm_app.get_state(config)
    return state.values.get("messages", []) if state.values else []
