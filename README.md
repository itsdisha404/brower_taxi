# 🤖 BrowserAuto - Multi-Agent Computer Control System# 🤖 BrowserAuto - Multi-Agent Computer Control System# Alice & Bob Multi-Agent Chat System



[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)

[![Django 5.2.8](https://img.shields.io/badge/Django-5.2.8-green.svg)](https://www.djangoproject.com/)

[![LangChain](https://img.shields.io/badge/LangChain-Powered-orange.svg)](https://python.langchain.com/)An intelligent automation system that can **SEE, THINK, and ACT** on your computer using a multi-agent swarm architecture powered by Google Gemini AI.A Django-based chat application using LangGraph Swarm for multi-agent AI conversations with Gemini.

[![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)]()



> An intelligent automation system that can **SEE, THINK, and ACT** on your computer using a multi-agent swarm architecture powered by Google Gemini AI.

## 🌟 Overview## Project Structure

![BrowserAuto Demo](https://img.shields.io/badge/Status-Active-success)



---

BrowserAuto is an advanced computer automation system that uses AI agents to control your computer through natural language commands. The system can see your screen, understand what's happening, and perform actions just like a human would.```

## 📋 Table of Contents

browserauto/

- [Overview](#-overview)

- [Features](#-key-features)**Key Features:**├── core/

- [Technology Stack](#️-technology-stack)

- [Architecture](#️-architecture)- 👁️ **Vision System**: Captures and analyzes screen content in real-time│   ├── agents.py          # Agent initialization and swarm configuration

- [Installation](#-installation)

- [Usage](#-usage)- 🧠 **Multi-Agent Intelligence**: 4 specialized agents working together│   ├── tools.py           # Tools available to agents (add, subtract, multiply)

- [Configuration](#️-configuration)

- [Testing](#-testing)- ⚡ **Universal Control**: Works with ANY application (Chrome, Excel, Notepad, etc.)│   ├── prompts.py         # Agent prompts and personalities

- [Troubleshooting](#-troubleshooting)

- [Contributing](#-contributing)- 🎯 **Natural Language**: Just tell it what you want in plain English│   ├── views.py           # Django views (API endpoint + web page)



---- 🔄 **See-Think-Act Loop**: Intelligent decision-making based on visual feedback│   ├── urls.py            # URL routing



## 🌟 Overview│   ├── templates/



**BrowserAuto** is an advanced computer automation system that uses AI agents to control your computer through natural language commands. The system can see your screen, understand what's happening, and perform actions just like a human would.---│   │   └── core/



### 💡 Key Features│   │       └── index.html # Chat interface UI



| Feature | Description |## 🛠️ Technology Stack│   └── .env               # Environment variables (GEMINI_API_KEY)

|---------|-------------|

| 👁️ **Vision System** | Captures and analyzes screen content in real-time |├── browserauto/

| 🧠 **Multi-Agent Intelligence** | 4 specialized agents working together |

| ⚡ **Universal Control** | Works with ANY application (Chrome, Excel, Notepad, etc.) |### **Core Framework**│   ├── settings.py        # Django settings

| 🎯 **Natural Language** | Just tell it what you want in plain English |

| 🔄 **See-Think-Act Loop** | Intelligent decision-making based on visual feedback |- **Python 3.13** - Modern Python for async and performance│   └── urls.py            # Main URL configuration



---- **Django 5.2.8** - Web framework for user interface├── manage.py              # Django management script



## 🛠️ Technology Stack- **LangChain** - Agent orchestration and tool management└── test_agents.py         # Test script for agents



### Core Framework- **LangGraph** - Agent workflow and state management```



```yaml- **LangGraph Swarm** - Multi-agent coordination system

Python: 3.13

Django: 5.2.8## Features

LangChain: Latest

LangGraph: Latest### **AI & Language Models**

LangGraph Swarm: 0.2.0

```- **Google Gemini AI** (`gemini-1.5-flash`)- **Alice**: Math expert agent with addition, subtraction, and multiplication tools



### AI & Language Models  - Model: `ChatGoogleGenerativeAI`- **Bob**: Friendly pirate assistant for general conversations



- **Google Gemini AI** (`gemini-1.5-flash`)  - Rate Limit: 1500 requests/day (free tier)- **Agent Handoffs**: Agents can transfer conversations to each other

  - Rate Limit: **1500 requests/day** (free tier)

  - Capabilities: Vision, reasoning, natural language understanding  - Capabilities: Vision, reasoning, natural language understanding- **Memory**: Conversation history maintained per thread

- **LangChain Google GenAI** - Integration layer

- **LangChain Google GenAI** - Integration layer for Gemini- **Real-time Chat**: Interactive web interface

### Computer Vision & Automation



```yaml

PyAutoGUI: 0.9.54      # Screen control & automation### **Computer Vision & Automation**## Setup

OpenCV-Python: 4.12.0  # Computer vision

Pillow (PIL): 12.0.0   # Image processing- **PyAutoGUI 0.9.54** - Screen control, mouse, and keyboard automation

NumPy: 2.2.6           # Numerical operations

```- **OpenCV-Python 4.12.0.88** - Computer vision and image analysis1. **Install Dependencies**:



### Supporting Libraries- **Pillow (PIL) 12.0.0** - Image processing and screenshot handling   ```bash



- `python-dotenv` - Environment management- **NumPy 2.2.6** - Numerical operations for screen analysis   pip install langgraph-swarm langchain-google-genai python-dotenv django

- `httpx` - HTTP client

- `selenium` - Browser automation (optional/legacy)   ```



---### **Web Automation** (Optional/Legacy)



## 🏗️ Architecture- **Selenium WebDriver** - Browser automation (deprecated in favor of universal control)2. **Configure API Key**:



### Multi-Agent Swarm System- **Chrome WebDriver** - Chrome-specific automation   Create `core/.env` file:



```   ```

┌─────────────────────────────────────────────────────────────┐

│                        User Request                          │### **Supporting Libraries**   GEMINI_API_KEY=your_gemini_api_key_here

└─────────────────────┬───────────────────────────────────────┘

                      │- **python-dotenv** - Environment variable management   ```

                      ▼

         ┌────────────────────────┐- **typing** - Type hints and annotations

         │  🎯 Coordinator Agent  │

         │  ┌──────────────────┐  │- **asyncio** - Asynchronous operations3. **Run Migrations** (optional):

         │  │ Entry point      │  │

         │  │ Breaks down task │  │- **re** (regex) - Pattern matching for command parsing   ```bash

         │  │ Delegates work   │  │

         │  └──────────────────┘  │   python manage.py migrate

         └────────┬───────────────┘

                  │---   ```

                  ▼

         ┌────────────────────────┐

         │  📋 TaskPlanner Agent  │

         │  ┌──────────────────┐  │## 🏗️ Architecture4. **Start Server**:

         │  │ Creates TODO     │  │

         │  │ Step-by-step     │  │   ```bash

         │  │ Sequencing       │  │

         │  └──────────────────┘  │### **Multi-Agent Swarm System**   python manage.py runserver

         └────────┬───────────────┘

                  │   ```

                  ▼

         ┌────────────────────────┐The system uses **4 specialized agents** that collaborate through a swarm architecture:

         │   ⚡ Executor Agent    │

         │  ┌──────────────────┐  │5. **Open Browser**:

         │  │ 👁️ SEE screen   │  │

         │  │ 🧠 THINK         │  │```   Navigate to `http://127.0.0.1:8000/`

         │  │ ⚡ ACT           │  │

         │  │ ✅ VERIFY        │  │User Request

         │  └──────────────────┘  │

         └────────┬───────────────┘     ↓## API Usage

                  │

                  ▼[Coordinator] ──────→ Understands request & delegates

         ┌────────────────────────┐

         │   📊 Reporter Agent    │     ↓### Chat Endpoint

         │  ┌──────────────────┐  │

         │  │ Format results   │  │[TaskPlanner] ──────→ Creates detailed TODO list

         │  │ Screenshots      │  │

         │  │ Evidence         │  │     ↓**URL**: `POST /api/chat/`

         │  └──────────────────┘  │

         └────────┬───────────────┘[Executor] ─────────→ SEE → THINK → ACT loop

                  │

                  ▼     ↓                 ├─ see_screen() - Vision**Request**:

         ┌────────────────────────┐

         │     User receives      │     ↓                 ├─ perform_action() - Action```json

         │  detailed results with │

         │      screenshots       │     ↓                 └─ Mouse tools - Precision{

         └────────────────────────┘

```     ↓  "message": "what's 5 + 7?",



### Agent Roles[Reporter] ─────────→ Formats results with evidence  "thread_id": "user_123"



| Agent | Role | Tools |     ↓}

|-------|------|-------|

| **🎯 Coordinator** | Entry point, understands requests | Handoff tools |User receives results```

| **📋 TaskPlanner** | Creates detailed TODO lists | Handoff tools |

| **⚡ Executor** | Executes with vision-action loop | `see_screen`, `perform_action`, mouse tools |```

| **📊 Reporter** | Formats results with evidence | `see_screen`, `get_mouse_position` |

**Response**:

---

#### **Agent Roles:**```json

## 🔧 Core Tools

{

### 1️⃣ Vision Tool

1. **Coordinator Agent**  "success": true,

```python

see_screen(analysis_request: str) -> str   - Entry point for all user requests  "response": "The answer is 12.",

```

   - Breaks down complex tasks into objectives  "active_agent": "Alice",

**Purpose:** Captures and analyzes screen state

   - Delegates work to appropriate agents  "messages": [...]

**Returns:**

- Screen resolution & mouse position   - Tools: Handoff tools}

- Visible applications & UI elements

- Element coordinates```

- Recommendations for next action

2. **TaskPlanner Agent**

**Example:**

```python   - Creates detailed, step-by-step TODO lists## Testing

see_screen("Is Chrome open?")

see_screen("Where is the profile icon?")   - Formats instructions for Executor

see_screen("Find the address bar")

```   - Handles task breakdown and sequencingRun the test script:



---   - Tools: Handoff tools```bash



### 2️⃣ Action Toolpython test_agents.py



```python3. **Executor Agent** (The Workhorse)```

perform_action(action_description: str) -> str

```   - **SEES** the screen using `see_screen()`



**Supported Actions:**   - **THINKS** about what to do next## Agents



| Action | Example |   - **ACTS** using `perform_action()`

|--------|---------|

| Open app | `open chrome` |   - Uses mouse tools for precision### Alice (Math Expert)

| Click | `click at coordinates 1820, 50` |

| Type | `type 'Hello World'` |   - Tools: `see_screen`, `perform_action`, `move_mouse`, `click_mouse`, `get_mouse_position`- **Tools**: add, subtract, multiply, handoff to Bob

| Press keys | `press ctrl+c` |

| Mouse move | `move mouse to 500, 300` |- **Specialty**: Mathematical operations and problem-solving

| Scroll | `scroll down` |

| Wait | `wait 2 seconds` |4. **Reporter Agent**- **Prompt**: Defined in `prompts.py`



---   - Formats execution results



### 3️⃣ Mouse Tools   - Provides evidence with screenshots### Bob (Pirate Assistant)



```python   - Comprehensive status reporting- **Tools**: handoff to Alice

move_mouse(x: int, y: int) -> str

click_mouse(x: int, y: int) -> str   - Tools: `see_screen`, `get_mouse_position`- **Specialty**: General conversations in pirate style

get_mouse_position() -> str

```- **Prompt**: Defined in `prompts.py`



---### **LangGraph Swarm Features**



## 📦 Installation## Customization



### Prerequisites- **`create_react_agent()`** - Creates ReAct (Reasoning + Acting) agents



- ✅ Python 3.13 or higher- **`create_handoff_tool()`** - Enables agent-to-agent communication### Adding New Tools

- ✅ Windows OS

- ✅ Google Gemini API Key ([Get one here](https://ai.google.dev/))- **`create_swarm()`** - Orchestrates multi-agent workflowsEdit `core/tools.py`:



### Quick Start- **State Management** - Maintains context across agent handoffs```python



```bash- **Automatic Tool Routing** - Smart tool selection per agentdef your_tool(param: type) -> return_type:

# 1. Navigate to project directory

cd d:\tp_project    """Tool description."""



# 2. Create virtual environment---    # Your implementation

python -m venv myenv

myenv\Scripts\Activate.ps1    return result



# 3. Install dependencies## 🔧 Core Tools```

pip install -r requirements.txt



# 4. Configure API key

# Create .env file in browserauto/ directory### **1. Vision Tool - `see_screen()`**### Modifying Prompts

echo GEMINI_API_KEY=your_api_key_here > browserauto\.env

```pythonEdit `core/prompts.py`:

# 5. Run migrations

cd browserautosee_screen(analysis_request: str) -> str```python

python manage.py migrate

```YOUR_AGENT_PROMPT = """Your custom prompt here"""

# 6. Start server

python manage.py runserver 8000- Captures current screen state```



# 7. Open browser- Analyzes based on request (e.g., "Is Chrome open?", "Where is the profile icon?")

# Navigate to: http://127.0.0.1:8000/

```- Returns detailed analysis with:### Adding New Agents



### Manual Installation  - Screen resolution and mouse positionEdit `core/agents.py` and add new agent configuration.



```bash  - Visible applications and UI elements

pip install django==5.2.8

pip install langchain langchain-google-genai langgraph langgraph-swarm  - Coordinates of important elements## Technologies Used

pip install pillow pyautogui opencv-python numpy

pip install python-dotenv  - Recommendations for next action

```

- **Django**: Web framework

---

**Technology:** PyAutoGUI (screenshot), OpenCV (analysis), NumPy (image processing)- **LangGraph Swarm**: Multi-agent orchestration

## 🚀 Usage

- **LangChain**: Agent framework

### Example Commands

### **2. Action Tool - `perform_action()`**- **Google Gemini**: LLM (gemini-2.0-flash-exp)

#### Simple Actions

``````python- **Python-dotenv**: Environment variable management

"Open Chrome"

"Open Notepad and type 'Hello World'"perform_action(action_description: str) -> str

"Open Calculator"

``````## Notes



#### Browser Automation- Executes actions based on natural language

```

"Open Chrome with KHAYALICO profile and go to LinkedIn"- Supported actions:- Each conversation thread maintains its own state

"Click on the profile icon, then select KHAYALICO"

```  - `open <application>` - Launch apps- Agents automatically transfer based on user requests



#### Complex Workflows  - `click at coordinates <x>, <y>` - Precise clicking- The system uses in-memory checkpointing (resets on server restart)

```

"Open Chrome, go to Gmail, compose a new email"  - `type '<text>'` - Text input- For production, consider using a persistent checkpoint backend

"Open Excel, create a new spreadsheet, save as 'Data.xlsx'"

"Search for 'Python tutorial' on Google and open first link"  - `press <keys>` - Keyboard shortcuts

```  - `move mouse to <x>, <y>` - Mouse movement

  - `scroll up/down` - Scrolling

### How It Works  - `wait <seconds>` - Delays

- Returns execution status with screenshot evidence

**Example Flow:**

**Technology:** PyAutoGUI (automation), regex (parsing), PIL (screenshots)

```

Command: "Open Chrome with KHAYALICO profile and go to LinkedIn"### **3. Mouse Tools**

```python

1. 🎯 Coordinator: "Break down this Chrome task"move_mouse(x: int, y: int) -> str

click_mouse(x: int, y: int) -> str

2. 📋 TaskPlanner: Creates TODO:get_mouse_position() -> str

   ✅ Check if Chrome is open```

   ✅ If not, open Chrome- Precise mouse control

   ✅ Find profile icon (coordinates)- Coordinate-based operations

   ✅ Click profile icon- Real-time position tracking

   ✅ Select KHAYALICO

   ✅ Navigate to linkedin.com**Technology:** PyAutoGUI



3. ⚡ Executor executes:---

   👁️ see_screen("Is Chrome open?")

   → "Chrome not visible"## 📦 Installation

   

   ⚡ perform_action("open chrome")### **Prerequisites**

   → Chrome opens (you see it!)- Python 3.13 or higher

   - Windows OS (current version)

   👁️ see_screen("Where is profile icon?")- Google Gemini API Key

   → "Profile icon at (1820, 50)"

   ### **Setup Steps**

   ⚡ perform_action("click at 1820, 50")

   → Profile menu opens1. **Clone the repository**

   ```powershell

   ... continues ...cd d:\tp_project

```

4. 📊 Reporter: "✅ Success! Chrome opened with KHAYALICO, LinkedIn loaded"

```2. **Create virtual environment**

```powershell

---python -m venv myenv

myenv\Scripts\Activate.ps1

## ⚙️ Configuration```



### Model Selection3. **Install dependencies**

```powershell

Edit `core/agents.py`:pip install django==5.2.8

pip install langchain langchain-google-genai langgraph langgraph-swarm

```pythonpip install pillow pyautogui opencv-python numpy

model = ChatGoogleGenerativeAI(pip install python-dotenv

    model="gemini-1.5-flash",  # or "gemini-2.0-flash-exp"pip install selenium  # Optional for legacy browser automation

    api_key=api_key,```

    convert_system_message_to_human=True

)4. **Configure API Key**

```Create `.env` file in `browserauto/` directory:

```

### Rate LimitsGEMINI_API_KEY=your_api_key_here

```

| Model | Requests/Day | RPM |

|-------|--------------|-----|Get your API key: https://ai.google.dev/

| `gemini-1.5-flash` | 1500 | 15 |

| `gemini-2.0-flash-exp` | 50 | 5 |5. **Run migrations**

```powershell

### Safety Settingscd browserauto

python manage.py migrate

In `tools.py`:```



```python6. **Start the server**

pyautogui.FAILSAFE = True  # Move mouse to corner to abort```powershell

pyautogui.PAUSE = 0.5      # Delay between actionspython manage.py runserver 8000

``````



---7. **Open in browser**

```

## 🔬 Testinghttp://127.0.0.1:8000/

```

### Test Scripts

---

```bash

# 1. Multi-agent swarm test## 🚀 Usage

python test_swarm_agents.py

### **Example Commands**

# 2. Live demo (Chrome + KHAYALICO + LinkedIn)

python demo_live_control.py**Simple Actions:**

```

# 3. Direct agent testing"Open Chrome"

python test_agents.py"Open Notepad and type 'Hello World'"

```"Open Calculator"

```

---

**Browser Automation:**

## 📁 Project Structure```

"Open Chrome with KHAYALICO profile and go to LinkedIn"

```"Open Chrome, switch to KHAYALICO profile, then navigate to linkedin.com"

browserauto/"Click on the profile icon, then select KHAYALICO"

├── 📂 core/```

│   ├── agents.py              # Multi-agent swarm config

│   ├── prompts.py             # Agent role definitions**Complex Workflows:**

│   ├── tools.py               # Vision & action tools```

│   ├── views.py               # Django views"Open Chrome, go to Gmail, compose a new email"

│   ├── urls.py                # URL routing"Open Excel, create a new spreadsheet, and save it as 'Data.xlsx'"

│   └── 📂 templates/"Search for 'Python tutorial' on Google and open the first link"

│       └── core/```

│           └── index.html     # Web interface

├── 📂 browserauto/### **How It Works**

│   ├── settings.py            # Django settings

│   ├── urls.py                # Main URL config1. **You type a command** in the web interface

│   └── wsgi.py                # WSGI config2. **Coordinator receives** and understands your request

├── manage.py                  # Django management3. **TaskPlanner creates** a detailed TODO list

├── requirements.txt           # Dependencies4. **Executor executes** using the see-think-act loop:

├── .env                       # API keys (not in repo)   - 👁️ Captures screen → Analyzes what's visible

└── README.md                  # This file   - 🧠 Thinks about next step

```   - ⚡ Performs action

   - ✅ Verifies result

---   - 🔄 Repeats until done

5. **Reporter formats** the results with screenshots

## 🐛 Troubleshooting6. **You see results** with detailed execution logs



### Issue: API Rate Limit Exceeded---



```## 🔬 Testing

Error: 429 You exceeded your current quota

```### **Test Scripts Included**



**Solution:**1. **`test_swarm_agents.py`** - Test the multi-agent swarm

- Wait for quota reset (daily at midnight)```powershell

- Switch to `gemini-1.5-flash` (1500 req/day)python test_swarm_agents.py

```

### Issue: Vision System Not Available

2. **`demo_live_control.py`** - Live demo of Chrome + KHAYALICO + LinkedIn

``````powershell

Error: Vision system not availablepython demo_live_control.py

``````



**Solution:**3. **Direct agent testing**

```bash```powershell

pip install pillow pyautogui opencv-python numpypython test_agents.py

``````



### Issue: Permission Errors---



**Solution:** Run terminal as Administrator## 📁 Project Structure



### Issue: Actions Too Fast```

browserauto/

**Solution:** Increase delay in `tools.py`:├── core/

```python│   ├── agents.py          # Multi-agent swarm configuration

pyautogui.PAUSE = 1.0  # Increase from 0.5│   ├── prompts.py         # Agent role definitions

```│   ├── tools.py           # Vision & action tools

│   ├── views.py           # Django views

---│   ├── urls.py            # URL routing

│   └── templates/

## 🎯 Key Advantages│       └── core/

│           └── index.html # Web interface

### ✅ See-Think-Act Loop├── browserauto/

Unlike traditional automation that blindly executes commands:│   ├── settings.py        # Django settings

│   ├── urls.py            # Main URL config

| Traditional | BrowserAuto |│   └── wsgi.py            # WSGI config

|-------------|-------------|├── manage.py              # Django management

| ❌ Hardcoded clicks | ✅ Sees screen first |├── db.sqlite3             # Database

| ❌ Blind execution | ✅ Thinks about context |├── .env                   # API keys (not in repo)

| ❌ No verification | ✅ Verifies each action |└── README.md              # This file

| ❌ Breaks easily | ✅ Adapts to changes |

myenv/                     # Virtual environment

### ✅ Universal Control└── ...



Works with **ANY** application:Documentation/

├── QUICKSTART.md

- ✅ Browsers (Chrome, Firefox, Edge)├── MULTI_AGENT_SWARM.md

- ✅ Office (Word, Excel, PowerPoint)├── AGENTS_UPGRADE_SUMMARY.md

- ✅ Utilities (Notepad, Calculator, File Explorer)└── ...

- ✅ Custom applications```



### ✅ Natural Language---



```diff## 🎯 Key Features Explained

- pyautogui.click(1820, 50); time.sleep(1); pyautogui.write('KHAYALICO')

+ "Click on profile icon and select KHAYALICO"### **1. See-Think-Act Loop**

```Unlike traditional automation that blindly executes commands, BrowserAuto:

- **Sees** what's actually on screen

---- **Thinks** about the current state

- **Acts** based on visual analysis

## 📚 Learning Resources- **Verifies** each action succeeded



- **LangChain:** https://python.langchain.com/docs/### **2. Universal Control**

- **LangGraph:** https://langchain-ai.github.io/langgraph/Not limited to browsers! Can control:

- **Google Gemini API:** https://ai.google.dev/docs- ✅ Chrome, Firefox, Edge

- **PyAutoGUI:** https://pyautogui.readthedocs.io/- ✅ Notepad, Word, Excel

- ✅ Calculator, File Explorer

---- ✅ Any Windows application



## 🚧 Roadmap### **3. Natural Language**

No coding required. Just describe what you want:

- [ ] OCR integration for text recognition- ❌ Bad: `pyautogui.click(1820, 50); time.sleep(1)`

- [ ] Image template matching- ✅ Good: `"Click on the profile icon"`

- [ ] Multi-monitor support

- [ ] Voice command input### **4. Visual Feedback**

- [ ] Automation recording & playback- All actions happen visibly on your screen

- [ ] OpenAI/Claude integration- Screenshots saved for verification

- [ ] Mobile device control (ADB)- Real-time status updates

- [ ] Scheduled tasks- You see exactly what the agent is doing



---### **5. Intelligent Error Handling**

- If action fails, agent uses vision to diagnose

## 🤝 Contributing- Tries alternative approaches

- Reports detailed error information

Contributions welcome! Areas for improvement:

---

1. 🎯 Better UI element detection

2. 🛡️ More robust error handling## ⚙️ Configuration

3. 🔧 Additional action types

4. ⚡ Performance optimizations### **Model Selection**

5. 📖 Documentation improvementsEdit `core/agents.py` to change AI model:

```python

---model = ChatGoogleGenerativeAI(

    model="gemini-1.5-flash",  # Options: gemini-1.5-flash, gemini-2.0-flash-exp

## 🔒 Security & Privacy    api_key=api_key,

    convert_system_message_to_human=True

- ✅ All processing happens **locally**)

- ✅ Only AI requests go to Google Gemini API```

- ✅ Screenshots saved **locally** (not uploaded)

- ✅ API key in `.env` (never commit to git)### **Rate Limits**

- ✅ No data collection or telemetry- **gemini-1.5-flash**: 1500 requests/day (free)

- **gemini-2.0-flash-exp**: 50 requests/day (free)

---

### **Safety Settings**

## 🙏 CreditsPyAutoGUI safety features (in `tools.py`):

```python

**Technologies:**pyautogui.FAILSAFE = True  # Move mouse to corner to abort

- [LangChain Team](https://langchain.com/) - Agent frameworkpyautogui.PAUSE = 0.5      # Delay between actions

- [Google](https://ai.google.dev/) - Gemini AI```

- [Django Software Foundation](https://www.djangoproject.com/) - Web framework

- [PyAutoGUI Team](https://pyautogui.readthedocs.io/) - Automation library---



**Version:** 1.0.0  ## 🐛 Troubleshooting

**Date:** November 2025

### **API Rate Limit Exceeded**

---```

Error: 429 You exceeded your current quota

## 📄 License```

**Solution:** Wait for reset or switch to `gemini-1.5-flash` in `agents.py`

This project is for **educational and personal use**.

### **Vision System Not Available**

---```

Error: Vision system not available

## 🎉 Quick Start Example```

**Solution:** Install missing packages:

```bash```powershell

# Start the serverpip install pillow pyautogui opencv-python numpy

python manage.py runserver 8000```



# Open browser: http://127.0.0.1:8000/### **Permission Errors**

Some actions may require administrator privileges.

# Try this command:**Solution:** Run terminal as Administrator

"Open Chrome with KHAYALICO profile and go to LinkedIn"

### **Actions Too Fast**

# Watch the magic happen! ✨Increase delay in `tools.py`:

# 1. Coordinator breaks down the task```python

# 2. TaskPlanner creates a TODO listpyautogui.PAUSE = 1.0  # Increase from 0.5 to 1.0

# 3. Executor sees your screen, thinks, and acts```

# 4. Reporter shows you the results

```---



---## 🔒 Security & Privacy



<div align="center">- All processing happens **locally** on your machine

- Only AI requests go to Google Gemini API

**🤖 Enjoy automating your computer with AI! ✨**- Screenshots are saved locally (not uploaded)

- API key stored in `.env` file (never commit to git)

[![GitHub](https://img.shields.io/badge/GitHub-Star-yellow.svg)](https://github.com)- No data collection or telemetry

[![Twitter](https://img.shields.io/badge/Twitter-Share-blue.svg)](https://twitter.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Share-blue.svg)](https://linkedin.com)---



</div>## 📚 LangChain & LangGraph Concepts


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
