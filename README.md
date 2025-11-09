# 🤖 BrowserAuto - Multi-Agent Computer Control System
<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/8863b99f-0f31-4f14-9122-7565353ea0ee" />



[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)

[![Django 5.2.8](https://img.shields.io/badge/Django-5.2.8-green.svg)](https://www.djangoproject.com/)

[![LangChain](https://img.shields.io/badge/LangChain-Powered-orange.svg)](https://python.langchain.com/)[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)

[![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)]()

[![Django 5.2.8](https://img.shields.io/badge/Django-5.2.8-green.svg)](https://www.djangoproject.com/)

> An intelligent automation system that can **SEE, THINK, and ACT** on your computer using a multi-agent swarm architecture powered by Google Gemini AI.

[![LangChain](https://img.shields.io/badge/LangChain-Powered-orange.svg)](https://python.langchain.com/)An intelligent automation system that can **SEE, THINK, and ACT** on your computer using a multi-agent swarm architecture powered by Google Gemini AI.A Django-based chat application using LangGraph Swarm for multi-agent AI conversations with Gemini.

![BrowserAuto Demo](https://img.shields.io/badge/Status-Active-success)

[![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)]()

---



## 📋 Table of Contents

> An intelligent automation system that can **SEE, THINK, and ACT** on your computer using a multi-agent swarm architecture powered by Google Gemini AI.

- [Overview](#-overview)

- [Key Features](#-key-features)## 🌟 Overview## Project Structure

- [Technology Stack](#-technology-stack)

- [Architecture](#-architecture)![BrowserAuto Demo](https://img.shields.io/badge/Status-Active-success)

- [Core Tools](#-core-tools)

- [Installation](#-installation)

- [Usage](#-usage)

- [Configuration](#-configuration)---

- [Testing](#-testing)

- [Project Structure](#-project-structure)BrowserAuto is an advanced computer automation system that uses AI agents to control your computer through natural language commands. The system can see your screen, understand what's happening, and perform actions just like a human would.```

- [Troubleshooting](#-troubleshooting)

- [Key Advantages](#-key-advantages)## 📋 Table of Contents

- [Learning Resources](#-learning-resources)

- [Contributing](#-contributing)browserauto/

- [Credits](#-credits)

- [Overview](#-overview)

---

- [Features](#-key-features)**Key Features:**├── core/

## 🌟 Overview

- [Technology Stack](#️-technology-stack)

**BrowserAuto** is an advanced computer automation system that uses AI agents to control your computer through natural language commands. The system can see your screen, understand what's happening, and perform actions just like a human would.

- [Architecture](#️-architecture)- 👁️ **Vision System**: Captures and analyzes screen content in real-time│   ├── agents.py          # Agent initialization and swarm configuration

---

- [Installation](#-installation)

## 💡 Key Features

- [Usage](#-usage)- 🧠 **Multi-Agent Intelligence**: 4 specialized agents working together│   ├── tools.py           # Tools available to agents (add, subtract, multiply)

<table>

<tr>- [Configuration](#️-configuration)

<td><strong>👁️ Vision System</strong></td>

<td>Captures and analyzes screen content in real-time</td>- [Testing](#-testing)- ⚡ **Universal Control**: Works with ANY application (Chrome, Excel, Notepad, etc.)│   ├── prompts.py         # Agent prompts and personalities

</tr>

<tr>- [Troubleshooting](#-troubleshooting)

<td><strong>🧠 Multi-Agent Intelligence</strong></td>

<td>4 specialized agents working together</td>- [Contributing](#-contributing)- 🎯 **Natural Language**: Just tell it what you want in plain English│   ├── views.py           # Django views (API endpoint + web page)

</tr>

<tr>

<td><strong>⚡ Universal Control</strong></td>

<td>Works with ANY application (Chrome, Excel, Notepad, etc.)</td>---- 🔄 **See-Think-Act Loop**: Intelligent decision-making based on visual feedback│   ├── urls.py            # URL routing

</tr>

<tr>

<td><strong>🎯 Natural Language</strong></td>

<td>Just tell it what you want in plain English</td>## 🌟 Overview│   ├── templates/

</tr>

<tr>

<td><strong>🔄 See-Think-Act Loop</strong></td>

<td>Intelligent decision-making based on visual feedback</td>**BrowserAuto** is an advanced computer automation system that uses AI agents to control your computer through natural language commands. The system can see your screen, understand what's happening, and perform actions just like a human would.---│   │   └── core/

</tr>

</table>



---### 💡 Key Features│   │       └── index.html # Chat interface UI



## 🛠️ Technology Stack



### Core Framework| Feature | Description |## 🛠️ Technology Stack│   └── .env               # Environment variables (GEMINI_API_KEY)



- **Python 3.13** - Modern Python for async and performance|---------|-------------|

- **Django 5.2.8** - Web framework for user interface

- **LangChain** - Agent orchestration and tool management| 👁️ **Vision System** | Captures and analyzes screen content in real-time |├── browserauto/

- **LangGraph** - Agent workflow and state management

- **LangGraph Swarm 0.2.0** - Multi-agent coordination system| 🧠 **Multi-Agent Intelligence** | 4 specialized agents working together |



### AI & Language Models| ⚡ **Universal Control** | Works with ANY application (Chrome, Excel, Notepad, etc.) |### **Core Framework**│   ├── settings.py        # Django settings



- **Google Gemini AI** (`gemini-1.5-flash`)| 🎯 **Natural Language** | Just tell it what you want in plain English |

  - Rate Limit: **1500 requests/day** (free tier)

  - Capabilities: Vision, reasoning, natural language understanding| 🔄 **See-Think-Act Loop** | Intelligent decision-making based on visual feedback |- **Python 3.13** - Modern Python for async and performance│   └── urls.py            # Main URL configuration

- **LangChain Google GenAI** - Integration layer



### Computer Vision & Automation

---- **Django 5.2.8** - Web framework for user interface├── manage.py              # Django management script

- **PyAutoGUI 0.9.54** - Screen control & automation

- **OpenCV-Python 4.12.0** - Computer vision

- **Pillow (PIL) 12.0.0** - Image processing

- **NumPy 2.2.6** - Numerical operations## 🛠️ Technology Stack- **LangChain** - Agent orchestration and tool management└── test_agents.py         # Test script for agents



### Supporting Libraries



- **python-dotenv** - Environment management### Core Framework- **LangGraph** - Agent workflow and state management```

- **httpx** - HTTP client

- **selenium** - Browser automation (optional/legacy)



---```yaml- **LangGraph Swarm** - Multi-agent coordination system



## 🏗️ ArchitecturePython: 3.13



### Multi-Agent Swarm SystemDjango: 5.2.8## Features



The system uses **4 specialized agents** that collaborate through a swarm architecture:LangChain: Latest



```LangGraph: Latest### **AI & Language Models**

User Request

     ↓LangGraph Swarm: 0.2.0

🎯 Coordinator Agent

  → Understands request```- **Google Gemini AI** (`gemini-1.5-flash`)- **Alice**: Math expert agent with addition, subtraction, and multiplication tools

  → Breaks down tasks

  → Delegates work

     ↓

📋 TaskPlanner Agent### AI & Language Models  - Model: `ChatGoogleGenerativeAI`- **Bob**: Friendly pirate assistant for general conversations

  → Creates TODO lists

  → Step-by-step planning

  → Task sequencing

     ↓- **Google Gemini AI** (`gemini-1.5-flash`)  - Rate Limit: 1500 requests/day (free tier)- **Agent Handoffs**: Agents can transfer conversations to each other

⚡ Executor Agent

  → 👁️ SEES screen  - Rate Limit: **1500 requests/day** (free tier)

  → 🧠 THINKS about action

  → ⚡ ACTS on decision  - Capabilities: Vision, reasoning, natural language understanding  - Capabilities: Vision, reasoning, natural language understanding- **Memory**: Conversation history maintained per thread

  → ✅ VERIFIES result

     ↓- **LangChain Google GenAI** - Integration layer

📊 Reporter Agent

  → Formats results- **LangChain Google GenAI** - Integration layer for Gemini- **Real-time Chat**: Interactive web interface

  → Adds screenshots

  → Provides evidence### Computer Vision & Automation

     ↓

User receives detailed results

```

```yaml

### Agent Roles

PyAutoGUI: 0.9.54      # Screen control & automation### **Computer Vision & Automation**## Setup

<table>

<thead>OpenCV-Python: 4.12.0  # Computer vision

<tr>

<th>Agent</th>Pillow (PIL): 12.0.0   # Image processing- **PyAutoGUI 0.9.54** - Screen control, mouse, and keyboard automation

<th>Role</th>

<th>Tools</th>NumPy: 2.2.6           # Numerical operations

</tr>

</thead>```- **OpenCV-Python 4.12.0.88** - Computer vision and image analysis1. **Install Dependencies**:

<tbody>

<tr>

<td><strong>🎯 Coordinator</strong></td>

<td>Entry point, understands requests</td>### Supporting Libraries- **Pillow (PIL) 12.0.0** - Image processing and screenshot handling   ```bash

<td>Handoff tools</td>

</tr>

<tr>

<td><strong>📋 TaskPlanner</strong></td>- `python-dotenv` - Environment management- **NumPy 2.2.6** - Numerical operations for screen analysis   pip install langgraph-swarm langchain-google-genai python-dotenv django

<td>Creates detailed TODO lists</td>

<td>Handoff tools</td>- `httpx` - HTTP client

</tr>

<tr>- `selenium` - Browser automation (optional/legacy)   ```

<td><strong>⚡ Executor</strong></td>

<td>Executes with vision-action loop</td>

<td>see_screen, perform_action, mouse tools</td>

</tr>---### **Web Automation** (Optional/Legacy)

<tr>

<td><strong>📊 Reporter</strong></td>

<td>Formats results with evidence</td>

<td>see_screen, get_mouse_position</td>## 🏗️ Architecture- **Selenium WebDriver** - Browser automation (deprecated in favor of universal control)2. **Configure API Key**:

</tr>

</tbody>

</table>

### Multi-Agent Swarm System- **Chrome WebDriver** - Chrome-specific automation   Create `core/.env` file:

---



## 🔧 Core Tools

```   ```

### 1️⃣ Vision Tool

┌─────────────────────────────────────────────────────────────┐

```python

see_screen(analysis_request: str) -> str│                        User Request                          │### **Supporting Libraries**   GEMINI_API_KEY=your_gemini_api_key_here

```

└─────────────────────┬───────────────────────────────────────┘

**Purpose:** Captures and analyzes screen state

                      │- **python-dotenv** - Environment variable management   ```

**Returns:**

- Screen resolution & mouse position                      ▼

- Visible applications & UI elements

- Element coordinates         ┌────────────────────────┐- **typing** - Type hints and annotations

- Recommendations for next action

         │  🎯 Coordinator Agent  │

**Example:**

```python         │  ┌──────────────────┐  │- **asyncio** - Asynchronous operations3. **Run Migrations** (optional):

see_screen("Is Chrome open?")

see_screen("Where is the profile icon?")         │  │ Entry point      │  │

see_screen("Find the address bar")

```         │  │ Breaks down task │  │- **re** (regex) - Pattern matching for command parsing   ```bash



---         │  │ Delegates work   │  │



### 2️⃣ Action Tool         │  └──────────────────┘  │   python manage.py migrate



```python         └────────┬───────────────┘

perform_action(action_description: str) -> str

```                  │---   ```



**Supported Actions:**                  ▼



<table>         ┌────────────────────────┐

<thead>

<tr>         │  📋 TaskPlanner Agent  │

<th>Action</th>

<th>Example</th>         │  ┌──────────────────┐  │## 🏗️ Architecture4. **Start Server**:

</tr>

</thead>         │  │ Creates TODO     │  │

<tbody>

<tr>         │  │ Step-by-step     │  │   ```bash

<td>Open app</td>

<td><code>open chrome</code></td>         │  │ Sequencing       │  │

</tr>

<tr>         │  └──────────────────┘  │### **Multi-Agent Swarm System**   python manage.py runserver

<td>Click</td>

<td><code>click at coordinates 1820, 50</code></td>         └────────┬───────────────┘

</tr>

<tr>                  │   ```

<td>Type</td>

<td><code>type 'Hello World'</code></td>                  ▼

</tr>

<tr>         ┌────────────────────────┐The system uses **4 specialized agents** that collaborate through a swarm architecture:

<td>Press keys</td>

<td><code>press ctrl+c</code></td>         │   ⚡ Executor Agent    │

</tr>

<tr>         │  ┌──────────────────┐  │5. **Open Browser**:

<td>Mouse move</td>

<td><code>move mouse to 500, 300</code></td>         │  │ 👁️ SEE screen   │  │

</tr>

<tr>         │  │ 🧠 THINK         │  │```   Navigate to `http://127.0.0.1:8000/`

<td>Scroll</td>

<td><code>scroll down</code></td>         │  │ ⚡ ACT           │  │

</tr>

<tr>         │  │ ✅ VERIFY        │  │User Request

<td>Wait</td>

<td><code>wait 2 seconds</code></td>         │  └──────────────────┘  │

</tr>

</tbody>         └────────┬───────────────┘     ↓## API Usage

</table>

                  │

---

                  ▼[Coordinator] ──────→ Understands request & delegates

### 3️⃣ Mouse Tools

         ┌────────────────────────┐

```python

move_mouse(x: int, y: int) -> str         │   📊 Reporter Agent    │     ↓### Chat Endpoint

click_mouse(x: int, y: int) -> str

get_mouse_position() -> str         │  ┌──────────────────┐  │

```

         │  │ Format results   │  │[TaskPlanner] ──────→ Creates detailed TODO list

- Precise mouse control

- Coordinate-based operations         │  │ Screenshots      │  │

- Real-time position tracking

         │  │ Evidence         │  │     ↓**URL**: `POST /api/chat/`

---

         │  └──────────────────┘  │

## 📦 Installation

         └────────┬───────────────┘[Executor] ─────────→ SEE → THINK → ACT loop

### Prerequisites

                  │

✅ Python 3.13 or higher  

✅ Windows OS                    ▼     ↓                 ├─ see_screen() - Vision**Request**:

✅ Google Gemini API Key ([Get one here](https://ai.google.dev/))

         ┌────────────────────────┐

### Quick Start

         │     User receives      │     ↓                 ├─ perform_action() - Action```json

```bash

# 1. Navigate to project directory         │  detailed results with │

cd d:\tp_project

         │      screenshots       │     ↓                 └─ Mouse tools - Precision{

# 2. Create virtual environment

python -m venv myenv         └────────────────────────┘

myenv\Scripts\Activate.ps1

```     ↓  "message": "what's 5 + 7?",

# 3. Install dependencies

pip install -r requirements.txt



# 4. Configure API key### Agent Roles[Reporter] ─────────→ Formats results with evidence  "thread_id": "user_123"

# Create .env file in browserauto/ directory

echo GEMINI_API_KEY=your_api_key_here > browserauto\.env



# 5. Run migrations| Agent | Role | Tools |     ↓}

cd browserauto

python manage.py migrate|-------|------|-------|



# 6. Start server| **🎯 Coordinator** | Entry point, understands requests | Handoff tools |User receives results```

python manage.py runserver 8000

| **📋 TaskPlanner** | Creates detailed TODO lists | Handoff tools |

# 7. Open browser

# Navigate to: http://127.0.0.1:8000/| **⚡ Executor** | Executes with vision-action loop | `see_screen`, `perform_action`, mouse tools |```

```

| **📊 Reporter** | Formats results with evidence | `see_screen`, `get_mouse_position` |

### Manual Installation

**Response**:

```bash

pip install django==5.2.8---

pip install langchain langchain-google-genai langgraph langgraph-swarm

pip install pillow pyautogui opencv-python numpy#### **Agent Roles:**```json

pip install python-dotenv

```## 🔧 Core Tools



---{



## 🚀 Usage### 1️⃣ Vision Tool



### Example Commands1. **Coordinator Agent**  "success": true,



**Simple Actions:**```python

```

"Open Chrome"see_screen(analysis_request: str) -> str   - Entry point for all user requests  "response": "The answer is 12.",

"Open Notepad and type 'Hello World'"

"Open Calculator"```

```

   - Breaks down complex tasks into objectives  "active_agent": "Alice",

**Browser Automation:**

```**Purpose:** Captures and analyzes screen state

"Open Chrome with KHAYALICO profile and go to LinkedIn"

"Click on the profile icon, then select KHAYALICO"   - Delegates work to appropriate agents  "messages": [...]

```

**Returns:**

**Complex Workflows:**

```- Screen resolution & mouse position   - Tools: Handoff tools}

"Open Chrome, go to Gmail, compose a new email"

"Open Excel, create a new spreadsheet, save as 'Data.xlsx'"- Visible applications & UI elements

"Search for 'Python tutorial' on Google and open first link"

```- Element coordinates```



### How It Works- Recommendations for next action



**Example Flow:**2. **TaskPlanner Agent**



```**Example:**

Command: "Open Chrome with KHAYALICO profile and go to LinkedIn"

```python   - Creates detailed, step-by-step TODO lists## Testing

Step 1 - 🎯 Coordinator

"Break down this Chrome task"see_screen("Is Chrome open?")



Step 2 - 📋 TaskPlanner creates TODO:see_screen("Where is the profile icon?")   - Formats instructions for Executor

✅ Check if Chrome is open

✅ If not, open Chromesee_screen("Find the address bar")

✅ Find profile icon (coordinates)

✅ Click profile icon```   - Handles task breakdown and sequencingRun the test script:

✅ Select KHAYALICO

✅ Navigate to linkedin.com



Step 3 - ⚡ Executor executes:---   - Tools: Handoff tools```bash

👁️ see_screen("Is Chrome open?")

→ "Chrome not visible"



⚡ perform_action("open chrome")### 2️⃣ Action Toolpython test_agents.py

→ Chrome opens (you see it!)



👁️ see_screen("Where is profile icon?")

→ "Profile icon at (1820, 50)"```python3. **Executor Agent** (The Workhorse)```



⚡ perform_action("click at 1820, 50")perform_action(action_description: str) -> str

→ Profile menu opens

```   - **SEES** the screen using `see_screen()`

... continues through each step ...



Step 4 - 📊 Reporter

"✅ Success! Chrome opened with KHAYALICO, LinkedIn loaded"**Supported Actions:**   - **THINKS** about what to do next## Agents

```



---

| Action | Example |   - **ACTS** using `perform_action()`

## ⚙️ Configuration

|--------|---------|

### Model Selection

| Open app | `open chrome` |   - Uses mouse tools for precision### Alice (Math Expert)

Edit `core/agents.py`:

| Click | `click at coordinates 1820, 50` |

```python

model = ChatGoogleGenerativeAI(| Type | `type 'Hello World'` |   - Tools: `see_screen`, `perform_action`, `move_mouse`, `click_mouse`, `get_mouse_position`- **Tools**: add, subtract, multiply, handoff to Bob

    model="gemini-1.5-flash",  # or "gemini-2.0-flash-exp"

    api_key=api_key,| Press keys | `press ctrl+c` |

    convert_system_message_to_human=True

)| Mouse move | `move mouse to 500, 300` |- **Specialty**: Mathematical operations and problem-solving

```

| Scroll | `scroll down` |

### Rate Limits

| Wait | `wait 2 seconds` |4. **Reporter Agent**- **Prompt**: Defined in `prompts.py`

<table>

<thead>

<tr>

<th>Model</th>---   - Formats execution results

<th>Requests/Day</th>

<th>RPM</th>

</tr>

</thead>### 3️⃣ Mouse Tools   - Provides evidence with screenshots### Bob (Pirate Assistant)

<tbody>

<tr>

<td><code>gemini-1.5-flash</code></td>

<td>1500</td>```python   - Comprehensive status reporting- **Tools**: handoff to Alice

<td>15</td>

</tr>move_mouse(x: int, y: int) -> str

<tr>

<td><code>gemini-2.0-flash-exp</code></td>click_mouse(x: int, y: int) -> str   - Tools: `see_screen`, `get_mouse_position`- **Specialty**: General conversations in pirate style

<td>50</td>

<td>5</td>get_mouse_position() -> str

</tr>

</tbody>```- **Prompt**: Defined in `prompts.py`

</table>



### Safety Settings

---### **LangGraph Swarm Features**

In `tools.py`:



```python

pyautogui.FAILSAFE = True  # Move mouse to corner to abort## 📦 Installation## Customization

pyautogui.PAUSE = 0.5      # Delay between actions

```



---### Prerequisites- **`create_react_agent()`** - Creates ReAct (Reasoning + Acting) agents



## 🔬 Testing



### Test Scripts- ✅ Python 3.13 or higher- **`create_handoff_tool()`** - Enables agent-to-agent communication### Adding New Tools



```bash- ✅ Windows OS

# 1. Multi-agent swarm test

python test_swarm_agents.py- ✅ Google Gemini API Key ([Get one here](https://ai.google.dev/))- **`create_swarm()`** - Orchestrates multi-agent workflowsEdit `core/tools.py`:



# 2. Live demo (Chrome + KHAYALICO + LinkedIn)

python demo_live_control.py

### Quick Start- **State Management** - Maintains context across agent handoffs```python

# 3. Direct agent testing

python test_agents.py

```

```bash- **Automatic Tool Routing** - Smart tool selection per agentdef your_tool(param: type) -> return_type:

---

# 1. Navigate to project directory

## 📁 Project Structure

cd d:\tp_project    """Tool description."""

```

browserauto/

├── core/

│   ├── agents.py              # Multi-agent swarm config# 2. Create virtual environment---    # Your implementation

│   ├── prompts.py             # Agent role definitions

│   ├── tools.py               # Vision & action toolspython -m venv myenv

│   ├── views.py               # Django views

│   ├── urls.py                # URL routingmyenv\Scripts\Activate.ps1    return result

│   └── templates/

│       └── core/

│           └── index.html     # Web interface

├── browserauto/# 3. Install dependencies## 🔧 Core Tools```

│   ├── settings.py            # Django settings

│   ├── urls.py                # Main URL configpip install -r requirements.txt

│   └── wsgi.py                # WSGI config

├── manage.py                  # Django management

├── requirements.txt           # Dependencies

├── .env                       # API keys (not in repo)# 4. Configure API key

└── README.md                  # This file

```# Create .env file in browserauto/ directory### **1. Vision Tool - `see_screen()`**### Modifying Prompts



---echo GEMINI_API_KEY=your_api_key_here > browserauto\.env



## 🐛 Troubleshooting```pythonEdit `core/prompts.py`:



### API Rate Limit Exceeded# 5. Run migrations



```cd browserautosee_screen(analysis_request: str) -> str```python

Error: 429 You exceeded your current quota

```python manage.py migrate



**Solution:**```YOUR_AGENT_PROMPT = """Your custom prompt here"""

- Wait for quota reset (daily at midnight)

- Switch to `gemini-1.5-flash` (1500 req/day)# 6. Start server



### Vision System Not Availablepython manage.py runserver 8000- Captures current screen state```



```

Error: Vision system not available

```# 7. Open browser- Analyzes based on request (e.g., "Is Chrome open?", "Where is the profile icon?")



**Solution:**# Navigate to: http://127.0.0.1:8000/

```bash

pip install pillow pyautogui opencv-python numpy```- Returns detailed analysis with:### Adding New Agents

```



### Permission Errors

### Manual Installation  - Screen resolution and mouse positionEdit `core/agents.py` and add new agent configuration.

**Solution:** Run terminal as Administrator



### Actions Too Fast

```bash  - Visible applications and UI elements

**Solution:** Increase delay in `tools.py`:

```pythonpip install django==5.2.8

pyautogui.PAUSE = 1.0  # Increase from 0.5

```pip install langchain langchain-google-genai langgraph langgraph-swarm  - Coordinates of important elements## Technologies Used



---pip install pillow pyautogui opencv-python numpy



## 🎯 Key Advantagespip install python-dotenv  - Recommendations for next action



### ✅ See-Think-Act Loop```



Unlike traditional automation that blindly executes commands:- **Django**: Web framework



<table>---

<thead>

<tr>**Technology:** PyAutoGUI (screenshot), OpenCV (analysis), NumPy (image processing)- **LangGraph Swarm**: Multi-agent orchestration

<th>Traditional</th>

<th>BrowserAuto</th>## 🚀 Usage

</tr>

</thead>- **LangChain**: Agent framework

<tbody>

<tr>### Example Commands

<td>❌ Hardcoded clicks</td>

<td>✅ Sees screen first</td>### **2. Action Tool - `perform_action()`**- **Google Gemini**: LLM (gemini-2.0-flash-exp)

</tr>

<tr>#### Simple Actions

<td>❌ Blind execution</td>

<td>✅ Thinks about context</td>``````python- **Python-dotenv**: Environment variable management

</tr>

<tr>"Open Chrome"

<td>❌ No verification</td>

<td>✅ Verifies each action</td>"Open Notepad and type 'Hello World'"perform_action(action_description: str) -> str

</tr>

<tr>"Open Calculator"

<td>❌ Breaks easily</td>

<td>✅ Adapts to changes</td>``````## Notes

</tr>

</tbody>

</table>

#### Browser Automation- Executes actions based on natural language

### ✅ Universal Control

```

Works with **ANY** application:

"Open Chrome with KHAYALICO profile and go to LinkedIn"- Supported actions:- Each conversation thread maintains its own state

- ✅ Browsers (Chrome, Firefox, Edge)

- ✅ Office (Word, Excel, PowerPoint)"Click on the profile icon, then select KHAYALICO"

- ✅ Utilities (Notepad, Calculator, File Explorer)

- ✅ Custom applications```  - `open <application>` - Launch apps- Agents automatically transfer based on user requests



### ✅ Natural Language



Instead of writing complex code:#### Complex Workflows  - `click at coordinates <x>, <y>` - Precise clicking- The system uses in-memory checkpointing (resets on server restart)

```diff

- pyautogui.click(1820, 50); time.sleep(1); pyautogui.write('KHAYALICO')```

+ "Click on profile icon and select KHAYALICO"

```"Open Chrome, go to Gmail, compose a new email"  - `type '<text>'` - Text input- For production, consider using a persistent checkpoint backend



---"Open Excel, create a new spreadsheet, save as 'Data.xlsx'"



## 📚 Learning Resources"Search for 'Python tutorial' on Google and open first link"  - `press <keys>` - Keyboard shortcuts



- **LangChain:** [https://python.langchain.com/docs/](https://python.langchain.com/docs/)```  - `move mouse to <x>, <y>` - Mouse movement

- **LangGraph:** [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)

- **Google Gemini API:** [https://ai.google.dev/docs](https://ai.google.dev/docs)  - `scroll up/down` - Scrolling

- **PyAutoGUI:** [https://pyautogui.readthedocs.io/](https://pyautogui.readthedocs.io/)

### How It Works  - `wait <seconds>` - Delays

---

- Returns execution status with screenshot evidence

## 🚧 Roadmap

**Example Flow:**

- [ ] OCR integration for text recognition

- [ ] Image template matching**Technology:** PyAutoGUI (automation), regex (parsing), PIL (screenshots)

- [ ] Multi-monitor support

- [ ] Voice command input```

- [ ] Automation recording & playback

- [ ] OpenAI/Claude integrationCommand: "Open Chrome with KHAYALICO profile and go to LinkedIn"### **3. Mouse Tools**

- [ ] Mobile device control (ADB)

- [ ] Scheduled tasks```python



---1. 🎯 Coordinator: "Break down this Chrome task"move_mouse(x: int, y: int) -> str



## 🤝 Contributingclick_mouse(x: int, y: int) -> str



Contributions welcome! Areas for improvement:2. 📋 TaskPlanner: Creates TODO:get_mouse_position() -> str



1. 🎯 Better UI element detection   ✅ Check if Chrome is open```

2. 🛡️ More robust error handling

3. 🔧 Additional action types   ✅ If not, open Chrome- Precise mouse control

4. ⚡ Performance optimizations

5. 📖 Documentation improvements   ✅ Find profile icon (coordinates)- Coordinate-based operations



---   ✅ Click profile icon- Real-time position tracking



## 🔒 Security & Privacy   ✅ Select KHAYALICO



- ✅ All processing happens **locally**   ✅ Navigate to linkedin.com**Technology:** PyAutoGUI

- ✅ Only AI requests go to Google Gemini API

- ✅ Screenshots saved **locally** (not uploaded)

- ✅ API key in `.env` (never commit to git)

- ✅ No data collection or telemetry3. ⚡ Executor executes:---



---   👁️ see_screen("Is Chrome open?")



## 🙏 Credits   → "Chrome not visible"## 📦 Installation



**Technologies:**   

- [LangChain Team](https://langchain.com/) - Agent framework

- [Google](https://ai.google.dev/) - Gemini AI   ⚡ perform_action("open chrome")### **Prerequisites**

- [Django Software Foundation](https://www.djangoproject.com/) - Web framework

- [PyAutoGUI Team](https://pyautogui.readthedocs.io/) - Automation library   → Chrome opens (you see it!)- Python 3.13 or higher



**Version:** 1.0.0     - Windows OS (current version)

**Date:** November 2025

   👁️ see_screen("Where is profile icon?")- Google Gemini API Key

---

   → "Profile icon at (1820, 50)"

## 📄 License

   ### **Setup Steps**

This project is for **educational and personal use**.

   ⚡ perform_action("click at 1820, 50")

---

   → Profile menu opens1. **Clone the repository**

## 🎉 Quick Start Example

   ```powershell

```bash

# Start the server   ... continues ...cd d:\tp_project

python manage.py runserver 8000

```

# Open browser: http://127.0.0.1:8000/

4. 📊 Reporter: "✅ Success! Chrome opened with KHAYALICO, LinkedIn loaded"

# Try this command:

"Open Chrome with KHAYALICO profile and go to LinkedIn"```2. **Create virtual environment**



# Watch the magic happen! ✨```powershell

```

---python -m venv myenv

**What happens:**

1. **Coordinator** breaks down the taskmyenv\Scripts\Activate.ps1

2. **TaskPlanner** creates a TODO list

3. **Executor** sees your screen, thinks, and acts## ⚙️ Configuration```

4. **Reporter** shows you the results



---

### Model Selection3. **Install dependencies**

<div align="center">

```powershell

**🤖 Enjoy automating your computer with AI! ✨**

Edit `core/agents.py`:pip install django==5.2.8

[![GitHub](https://img.shields.io/badge/GitHub-Star-yellow.svg)](https://github.com)

[![Twitter](https://img.shields.io/badge/Twitter-Share-blue.svg)](https://twitter.com)pip install langchain langchain-google-genai langgraph langgraph-swarm

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Share-blue.svg)](https://linkedin.com)

```pythonpip install pillow pyautogui opencv-python numpy

</div>

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
