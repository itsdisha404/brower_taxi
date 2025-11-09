# Alice & Bob Multi-Agent Chat System

A Django-based chat application using LangGraph Swarm for multi-agent AI conversations with Gemini.

## Project Structure

```
browserauto/
├── core/
│   ├── agents.py          # Agent initialization and swarm configuration
│   ├── tools.py           # Tools available to agents (add, subtract, multiply)
│   ├── prompts.py         # Agent prompts and personalities
│   ├── views.py           # Django views (API endpoint + web page)
│   ├── urls.py            # URL routing
│   ├── templates/
│   │   └── core/
│   │       └── index.html # Chat interface UI
│   └── .env               # Environment variables (GEMINI_API_KEY)
├── browserauto/
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL configuration
├── manage.py              # Django management script
└── test_agents.py         # Test script for agents
```

## Features

- **Alice**: Math expert agent with addition, subtraction, and multiplication tools
- **Bob**: Friendly pirate assistant for general conversations
- **Agent Handoffs**: Agents can transfer conversations to each other
- **Memory**: Conversation history maintained per thread
- **Real-time Chat**: Interactive web interface

## Setup

1. **Install Dependencies**:
   ```bash
   pip install langgraph-swarm langchain-google-genai python-dotenv django
   ```

2. **Configure API Key**:
   Create `core/.env` file:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Run Migrations** (optional):
   ```bash
   python manage.py migrate
   ```

4. **Start Server**:
   ```bash
   python manage.py runserver
   ```

5. **Open Browser**:
   Navigate to `http://127.0.0.1:8000/`

## API Usage

### Chat Endpoint

**URL**: `POST /api/chat/`

**Request**:
```json
{
  "message": "what's 5 + 7?",
  "thread_id": "user_123"
}
```

**Response**:
```json
{
  "success": true,
  "response": "The answer is 12.",
  "active_agent": "Alice",
  "messages": [...]
}
```

## Testing

Run the test script:
```bash
python test_agents.py
```

## Agents

### Alice (Math Expert)
- **Tools**: add, subtract, multiply, handoff to Bob
- **Specialty**: Mathematical operations and problem-solving
- **Prompt**: Defined in `prompts.py`

### Bob (Pirate Assistant)
- **Tools**: handoff to Alice
- **Specialty**: General conversations in pirate style
- **Prompt**: Defined in `prompts.py`

## Customization

### Adding New Tools
Edit `core/tools.py`:
```python
def your_tool(param: type) -> return_type:
    """Tool description."""
    # Your implementation
    return result
```

### Modifying Prompts
Edit `core/prompts.py`:
```python
YOUR_AGENT_PROMPT = """Your custom prompt here"""
```

### Adding New Agents
Edit `core/agents.py` and add new agent configuration.

## Technologies Used

- **Django**: Web framework
- **LangGraph Swarm**: Multi-agent orchestration
- **LangChain**: Agent framework
- **Google Gemini**: LLM (gemini-2.0-flash-exp)
- **Python-dotenv**: Environment variable management

## Notes

- Each conversation thread maintains its own state
- Agents automatically transfer based on user requests
- The system uses in-memory checkpointing (resets on server restart)
- For production, consider using a persistent checkpoint backend
