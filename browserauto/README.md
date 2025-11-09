# 🤖 BrowserAuto - Multi-Agent Computer Control System# Alice & Bob Multi-Agent Chat System



An intelligent automation system that can **SEE, THINK, and ACT** on your computer using a multi-agent swarm architecture powered by Google Gemini AI.A Django-based chat application using LangGraph Swarm for multi-agent AI conversations with Gemini.



## 🌟 Overview## Project Structure



BrowserAuto is an advanced computer automation system that uses AI agents to control your computer through natural language commands. The system can see your screen, understand what's happening, and perform actions just like a human would.```

browserauto/

**Key Features:**├── core/

- 👁️ **Vision System**: Captures and analyzes screen content in real-time│   ├── agents.py          # Agent initialization and swarm configuration

- 🧠 **Multi-Agent Intelligence**: 4 specialized agents working together│   ├── tools.py           # Tools available to agents (add, subtract, multiply)

- ⚡ **Universal Control**: Works with ANY application (Chrome, Excel, Notepad, etc.)│   ├── prompts.py         # Agent prompts and personalities

- 🎯 **Natural Language**: Just tell it what you want in plain English│   ├── views.py           # Django views (API endpoint + web page)

- 🔄 **See-Think-Act Loop**: Intelligent decision-making based on visual feedback│   ├── urls.py            # URL routing

│   ├── templates/

---│   │   └── core/

│   │       └── index.html # Chat interface UI

## 🛠️ Technology Stack│   └── .env               # Environment variables (GEMINI_API_KEY)

├── browserauto/

### **Core Framework**│   ├── settings.py        # Django settings

- **Python 3.13** - Modern Python for async and performance│   └── urls.py            # Main URL configuration

- **Django 5.2.8** - Web framework for user interface├── manage.py              # Django management script

- **LangChain** - Agent orchestration and tool management└── test_agents.py         # Test script for agents

- **LangGraph** - Agent workflow and state management```

- **LangGraph Swarm** - Multi-agent coordination system

## Features

### **AI & Language Models**

- **Google Gemini AI** (`gemini-1.5-flash`)- **Alice**: Math expert agent with addition, subtraction, and multiplication tools

  - Model: `ChatGoogleGenerativeAI`- **Bob**: Friendly pirate assistant for general conversations

  - Rate Limit: 1500 requests/day (free tier)- **Agent Handoffs**: Agents can transfer conversations to each other

  - Capabilities: Vision, reasoning, natural language understanding- **Memory**: Conversation history maintained per thread

- **LangChain Google GenAI** - Integration layer for Gemini- **Real-time Chat**: Interactive web interface



### **Computer Vision & Automation**## Setup

- **PyAutoGUI 0.9.54** - Screen control, mouse, and keyboard automation

- **OpenCV-Python 4.12.0.88** - Computer vision and image analysis1. **Install Dependencies**:

- **Pillow (PIL) 12.0.0** - Image processing and screenshot handling   ```bash

- **NumPy 2.2.6** - Numerical operations for screen analysis   pip install langgraph-swarm langchain-google-genai python-dotenv django

   ```

### **Web Automation** (Optional/Legacy)

- **Selenium WebDriver** - Browser automation (deprecated in favor of universal control)2. **Configure API Key**:

- **Chrome WebDriver** - Chrome-specific automation   Create `core/.env` file:

   ```

### **Supporting Libraries**   GEMINI_API_KEY=your_gemini_api_key_here

- **python-dotenv** - Environment variable management   ```

- **typing** - Type hints and annotations

- **asyncio** - Asynchronous operations3. **Run Migrations** (optional):

- **re** (regex) - Pattern matching for command parsing   ```bash

   python manage.py migrate

---   ```



## 🏗️ Architecture4. **Start Server**:

   ```bash

### **Multi-Agent Swarm System**   python manage.py runserver

   ```

The system uses **4 specialized agents** that collaborate through a swarm architecture:

5. **Open Browser**:

```   Navigate to `http://127.0.0.1:8000/`

User Request

     ↓## API Usage

[Coordinator] ──────→ Understands request & delegates

     ↓### Chat Endpoint

[TaskPlanner] ──────→ Creates detailed TODO list

     ↓**URL**: `POST /api/chat/`

[Executor] ─────────→ SEE → THINK → ACT loop

     ↓                 ├─ see_screen() - Vision**Request**:

     ↓                 ├─ perform_action() - Action```json

     ↓                 └─ Mouse tools - Precision{

     ↓  "message": "what's 5 + 7?",

[Reporter] ─────────→ Formats results with evidence  "thread_id": "user_123"

     ↓}

User receives results```

```

**Response**:

#### **Agent Roles:**```json

{

1. **Coordinator Agent**  "success": true,

   - Entry point for all user requests  "response": "The answer is 12.",

   - Breaks down complex tasks into objectives  "active_agent": "Alice",

   - Delegates work to appropriate agents  "messages": [...]

   - Tools: Handoff tools}

```

2. **TaskPlanner Agent**

   - Creates detailed, step-by-step TODO lists## Testing

   - Formats instructions for Executor

   - Handles task breakdown and sequencingRun the test script:

   - Tools: Handoff tools```bash

python test_agents.py

3. **Executor Agent** (The Workhorse)```

   - **SEES** the screen using `see_screen()`

   - **THINKS** about what to do next## Agents

   - **ACTS** using `perform_action()`

   - Uses mouse tools for precision### Alice (Math Expert)

   - Tools: `see_screen`, `perform_action`, `move_mouse`, `click_mouse`, `get_mouse_position`- **Tools**: add, subtract, multiply, handoff to Bob

- **Specialty**: Mathematical operations and problem-solving

4. **Reporter Agent**- **Prompt**: Defined in `prompts.py`

   - Formats execution results

   - Provides evidence with screenshots### Bob (Pirate Assistant)

   - Comprehensive status reporting- **Tools**: handoff to Alice

   - Tools: `see_screen`, `get_mouse_position`- **Specialty**: General conversations in pirate style

- **Prompt**: Defined in `prompts.py`

### **LangGraph Swarm Features**

## Customization

- **`create_react_agent()`** - Creates ReAct (Reasoning + Acting) agents

- **`create_handoff_tool()`** - Enables agent-to-agent communication### Adding New Tools

- **`create_swarm()`** - Orchestrates multi-agent workflowsEdit `core/tools.py`:

- **State Management** - Maintains context across agent handoffs```python

- **Automatic Tool Routing** - Smart tool selection per agentdef your_tool(param: type) -> return_type:

    """Tool description."""

---    # Your implementation

    return result

## 🔧 Core Tools```



### **1. Vision Tool - `see_screen()`**### Modifying Prompts

```pythonEdit `core/prompts.py`:

see_screen(analysis_request: str) -> str```python

```YOUR_AGENT_PROMPT = """Your custom prompt here"""

- Captures current screen state```

- Analyzes based on request (e.g., "Is Chrome open?", "Where is the profile icon?")

- Returns detailed analysis with:### Adding New Agents

  - Screen resolution and mouse positionEdit `core/agents.py` and add new agent configuration.

  - Visible applications and UI elements

  - Coordinates of important elements## Technologies Used

  - Recommendations for next action

- **Django**: Web framework

**Technology:** PyAutoGUI (screenshot), OpenCV (analysis), NumPy (image processing)- **LangGraph Swarm**: Multi-agent orchestration

- **LangChain**: Agent framework

### **2. Action Tool - `perform_action()`**- **Google Gemini**: LLM (gemini-2.0-flash-exp)

```python- **Python-dotenv**: Environment variable management

perform_action(action_description: str) -> str

```## Notes

- Executes actions based on natural language

- Supported actions:- Each conversation thread maintains its own state

  - `open <application>` - Launch apps- Agents automatically transfer based on user requests

  - `click at coordinates <x>, <y>` - Precise clicking- The system uses in-memory checkpointing (resets on server restart)

  - `type '<text>'` - Text input- For production, consider using a persistent checkpoint backend

  - `press <keys>` - Keyboard shortcuts
  - `move mouse to <x>, <y>` - Mouse movement
  - `scroll up/down` - Scrolling
  - `wait <seconds>` - Delays
- Returns execution status with screenshot evidence

**Technology:** PyAutoGUI (automation), regex (parsing), PIL (screenshots)

### **3. Mouse Tools**
```python
move_mouse(x: int, y: int) -> str
click_mouse(x: int, y: int) -> str
get_mouse_position() -> str
```
- Precise mouse control
- Coordinate-based operations
- Real-time position tracking

**Technology:** PyAutoGUI

---

## 📦 Installation

### **Prerequisites**
- Python 3.13 or higher
- Windows OS (current version)
- Google Gemini API Key

### **Setup Steps**

1. **Clone the repository**
```powershell
cd d:\tp_project
```

2. **Create virtual environment**
```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
```

3. **Install dependencies**
```powershell
pip install django==5.2.8
pip install langchain langchain-google-genai langgraph langgraph-swarm
pip install pillow pyautogui opencv-python numpy
pip install python-dotenv
pip install selenium  # Optional for legacy browser automation
```

4. **Configure API Key**
Create `.env` file in `browserauto/` directory:
```
GEMINI_API_KEY=your_api_key_here
```

Get your API key: https://ai.google.dev/

5. **Run migrations**
```powershell
cd browserauto
python manage.py migrate
```

6. **Start the server**
```powershell
python manage.py runserver 8000
```

7. **Open in browser**
```
http://127.0.0.1:8000/
```

---

## 🚀 Usage

### **Example Commands**

**Simple Actions:**
```
"Open Chrome"
"Open Notepad and type 'Hello World'"
"Open Calculator"
```

**Browser Automation:**
```
"Open Chrome with KHAYALICO profile and go to LinkedIn"
"Open Chrome, switch to KHAYALICO profile, then navigate to linkedin.com"
"Click on the profile icon, then select KHAYALICO"
```

**Complex Workflows:**
```
"Open Chrome, go to Gmail, compose a new email"
"Open Excel, create a new spreadsheet, and save it as 'Data.xlsx'"
"Search for 'Python tutorial' on Google and open the first link"
```

### **How It Works**

1. **You type a command** in the web interface
2. **Coordinator receives** and understands your request
3. **TaskPlanner creates** a detailed TODO list
4. **Executor executes** using the see-think-act loop:
   - 👁️ Captures screen → Analyzes what's visible
   - 🧠 Thinks about next step
   - ⚡ Performs action
   - ✅ Verifies result
   - 🔄 Repeats until done
5. **Reporter formats** the results with screenshots
6. **You see results** with detailed execution logs

---

## 🔬 Testing

### **Test Scripts Included**

1. **`test_swarm_agents.py`** - Test the multi-agent swarm
```powershell
python test_swarm_agents.py
```

2. **`demo_live_control.py`** - Live demo of Chrome + KHAYALICO + LinkedIn
```powershell
python demo_live_control.py
```

3. **Direct agent testing**
```powershell
python test_agents.py
```

---

## 📁 Project Structure

```
browserauto/
├── core/
│   ├── agents.py          # Multi-agent swarm configuration
│   ├── prompts.py         # Agent role definitions
│   ├── tools.py           # Vision & action tools
│   ├── views.py           # Django views
│   ├── urls.py            # URL routing
│   └── templates/
│       └── core/
│           └── index.html # Web interface
├── browserauto/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL config
│   └── wsgi.py            # WSGI config
├── manage.py              # Django management
├── db.sqlite3             # Database
├── .env                   # API keys (not in repo)
└── README.md              # This file

myenv/                     # Virtual environment
└── ...

Documentation/
├── QUICKSTART.md
├── MULTI_AGENT_SWARM.md
├── AGENTS_UPGRADE_SUMMARY.md
└── ...
```

---

## 🎯 Key Features Explained

### **1. See-Think-Act Loop**
Unlike traditional automation that blindly executes commands, BrowserAuto:
- **Sees** what's actually on screen
- **Thinks** about the current state
- **Acts** based on visual analysis
- **Verifies** each action succeeded

### **2. Universal Control**
Not limited to browsers! Can control:
- ✅ Chrome, Firefox, Edge
- ✅ Notepad, Word, Excel
- ✅ Calculator, File Explorer
- ✅ Any Windows application

### **3. Natural Language**
No coding required. Just describe what you want:
- ❌ Bad: `pyautogui.click(1820, 50); time.sleep(1)`
- ✅ Good: `"Click on the profile icon"`

### **4. Visual Feedback**
- All actions happen visibly on your screen
- Screenshots saved for verification
- Real-time status updates
- You see exactly what the agent is doing

### **5. Intelligent Error Handling**
- If action fails, agent uses vision to diagnose
- Tries alternative approaches
- Reports detailed error information

---

## ⚙️ Configuration

### **Model Selection**
Edit `core/agents.py` to change AI model:
```python
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Options: gemini-1.5-flash, gemini-2.0-flash-exp
    api_key=api_key,
    convert_system_message_to_human=True
)
```

### **Rate Limits**
- **gemini-1.5-flash**: 1500 requests/day (free)
- **gemini-2.0-flash-exp**: 50 requests/day (free)

### **Safety Settings**
PyAutoGUI safety features (in `tools.py`):
```python
pyautogui.FAILSAFE = True  # Move mouse to corner to abort
pyautogui.PAUSE = 0.5      # Delay between actions
```

---

## 🐛 Troubleshooting

### **API Rate Limit Exceeded**
```
Error: 429 You exceeded your current quota
```
**Solution:** Wait for reset or switch to `gemini-1.5-flash` in `agents.py`

### **Vision System Not Available**
```
Error: Vision system not available
```
**Solution:** Install missing packages:
```powershell
pip install pillow pyautogui opencv-python numpy
```

### **Permission Errors**
Some actions may require administrator privileges.
**Solution:** Run terminal as Administrator

### **Actions Too Fast**
Increase delay in `tools.py`:
```python
pyautogui.PAUSE = 1.0  # Increase from 0.5 to 1.0
```

---

## 🔒 Security & Privacy

- All processing happens **locally** on your machine
- Only AI requests go to Google Gemini API
- Screenshots are saved locally (not uploaded)
- API key stored in `.env` file (never commit to git)
- No data collection or telemetry

---

## 📚 LangChain & LangGraph Concepts

### **ReAct Agents**
- **Re**asoning + **Act**ing pattern
- Agent thinks before each action
- Uses chain-of-thought prompting
- Function: `create_react_agent(model, tools, prompt)`

### **Agent Swarm**
- Multiple agents working together
- Each agent has specialized role
- Agents can hand off to each other
- Maintains shared state across handoffs

### **Tool System**
- Python functions decorated with `@tool`
- Type-annotated for LangChain
- Automatic schema generation
- Built-in error handling

---

## 🎓 Learning Resources

### **LangChain Documentation**
- https://python.langchain.com/docs/

### **LangGraph Documentation**
- https://langchain-ai.github.io/langgraph/

### **Google Gemini API**
- https://ai.google.dev/docs

### **PyAutoGUI Documentation**
- https://pyautogui.readthedocs.io/

---

## 🚧 Future Enhancements

- [ ] OCR integration for text recognition
- [ ] Image template matching for UI element detection
- [ ] Multi-monitor support
- [ ] Voice command input
- [ ] Recording and playback of automation sequences
- [ ] Integration with more AI models (OpenAI, Claude)
- [ ] Mobile device control via ADB
- [ ] Scheduled automation tasks

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Better UI element detection
- More robust error handling
- Additional action types
- Performance optimizations
- Documentation improvements

---

## 📄 License

This project is for educational and personal use.

---

## 🙏 Credits

**Technologies:**
- LangChain Team - Agent framework
- Google - Gemini AI
- Django Software Foundation - Web framework
- PyAutoGUI Team - Automation library

**Created by:** Your Name
**Date:** November 2025
**Version:** 1.0.0

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the documentation files
3. Test with simple commands first
4. Ensure API key is valid

---

## 🎉 Quick Start Example

```python
# After starting the server, try this in the web interface:
"Open Chrome with KHAYALICO profile and go to LinkedIn"

# What happens:
# 1. Coordinator: "I need to open Chrome with a specific profile"
# 2. TaskPlanner: Creates TODO:
#    - Check if Chrome is open
#    - If not, open Chrome
#    - Find profile icon
#    - Click profile icon
#    - Select KHAYALICO
#    - Navigate to linkedin.com
# 3. Executor: Executes each step with vision:
#    👁️ see_screen("Is Chrome open?")
#    ⚡ perform_action("open chrome")
#    👁️ see_screen("Where is profile icon?")
#    ⚡ perform_action("click at coordinates 1820, 50")
#    # ... continues until done
# 4. Reporter: "✅ Successfully opened Chrome with KHAYALICO and loaded LinkedIn"
```

---

**Enjoy automating your computer with AI! 🤖✨**
