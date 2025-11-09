# 🖥️ Universal Computer Control Tool

## Overview
Your AI agent can now **control your ENTIRE computer** using natural language! Watch your screen as the AI performs actions in real-time.

---

## 🌟 Main Feature: `computer_control(prompt)`

### The Universal Tool
This is the **primary tool** that can do anything on your computer. It:

1. **Parses** your natural language prompt into action steps
2. **Executes** each step visually on your screen
3. **You WATCH** everything happen in real-time
4. **Works** with ANY application - not just Chrome!

---

## 📋 What Can It Do?

### ✅ Open Applications
```python
computer_control("open chrome")
computer_control("open calculator")
computer_control("open notepad")
computer_control("open explorer")
computer_control("open word")
```

### ✅ Complex Multi-Step Actions
```python
# Open Chrome with specific profile
computer_control("open chrome, then click on profile icon, then select KHAYALICO")

# Full workflow
computer_control("open chrome, switch to KHAYALICO profile, then navigate to linkedin.com")

# Notepad workflow
computer_control("open notepad, then type 'Hello World', then save file")
```

### ✅ Click on Screen Elements
```python
computer_control("click on profile icon")
computer_control("click on search button")
computer_control("click on the sign in link")
```

### ✅ Type Text
```python
computer_control("type 'software engineer'")
computer_control("type 'hello@example.com' in the email field")
```

### ✅ Navigate & Switch
```python
computer_control("navigate to https://linkedin.com")
computer_control("switch to KHAYALICO profile")
computer_control("switch window")
```

### ✅ Search & Scroll
```python
computer_control("search for 'python'")
computer_control("scroll down")
computer_control("scroll up")
```

---

## 🎯 Your Specific Use Case

### Example: "Open Chrome in KHAYALICO Profile"

**Your Prompt:**
```python
computer_control("open chrome, then click on profile icon, then select KHAYALICO")
```

**What Happens:**
1. ✅ AI presses Windows key
2. ✅ Types "chrome"
3. ✅ Presses Enter (Chrome opens - YOU SEE IT)
4. ✅ Waits for Chrome to load
5. ✅ Clicks on profile icon (top-right corner)
6. ✅ Types "KHAYALICO"
7. ✅ Presses Enter to select profile
8. ✅ Takes screenshot of final state

**You watch every step happen on your screen!**

---

## 🔧 Additional Helper Tools

### 1. `screen_click(x, y)`
Click at exact coordinates
```python
screen_click(100, 200)  # Click at pixel position (100, 200)
```

### 2. `screen_type(text)`
Type text immediately
```python
screen_type("Hello World")
```

### 3. `press_keys(keys)`
Press keyboard shortcuts
```python
press_keys("enter")
press_keys("ctrl+c")  # Copy
press_keys("ctrl+v")  # Paste
press_keys("alt+tab")  # Switch window
press_keys("win")      # Windows key
```

### 4. `get_screen_info()`
Get current screen state
```python
get_screen_info()  # Returns screen size, mouse position, screenshot
```

---

## 🎬 How It Works

### Step-by-Step Breakdown

**Input Prompt:**
```
"open chrome, switch to KHAYALICO profile, then navigate to linkedin.com"
```

**AI Parsing:**
```
Step 1: OPEN - chrome
Step 2: SWITCH - KHAYALICO profile  
Step 3: NAVIGATE - linkedin.com
```

**Execution (YOU SEE THIS):**
```
✅ Step 1: Opened chrome
   [You see Chrome opening on your screen]

✅ Step 2: Switched to profile: KHAYALICO
   [You see profile being clicked and selected]

✅ Step 3: Navigated to: linkedin.com
   [You see browser navigating to LinkedIn]

📸 Final screenshot saved: current_screen.png
```

---

## 🚀 Getting Started

### Installation
All required packages are installed:
- ✅ `selenium` - Browser automation
- ✅ `pillow` - Image processing
- ✅ `pyautogui` - Screen control
- ✅ `opencv-python` - Computer vision
- ✅ `numpy` - Numerical operations

### Safety Features
1. **FAILSAFE**: Move mouse to top-left corner to stop immediately
2. **Delays**: Built-in pauses between actions for smooth control
3. **Screenshots**: Captures final state for verification
4. **Error Handling**: Graceful failure with detailed error messages

---

## 🧪 Testing

### Run the Test Suite
```bash
cd d:\tp_project\browserauto
python test_computer_control.py
```

### Test Scenarios Included
1. ✅ Open Chrome with KHAYALICO Profile
2. ✅ Open Calculator
3. ✅ Open Notepad and Type
4. ✅ Chrome + LinkedIn Navigation

---

## 📖 Usage Examples

### Example 1: Simple Application Launch
```python
from core.tools import computer_control

result = computer_control("open calculator")
print(result)

# Output:
# 🎯 Executing: open calculator
# 📋 Broken into 1 steps:
#    Step 1: OPEN - open calculator
# 
# 🚀 Executing actions (you will see them on screen):
# 
# ✅ Step 1: Opened calculator
# 📸 Final screenshot saved: current_screen.png
```

### Example 2: Complex Workflow
```python
result = computer_control("""
    open chrome,
    then click on profile,
    then select KHAYALICO,
    then navigate to linkedin.com
""")

# You will see:
# - Chrome opening
# - Profile menu clicking
# - KHAYALICO selection
# - LinkedIn loading
# ALL HAPPENING ON YOUR SCREEN!
```

### Example 3: With Agent
```python
# Your agent can now control the computer!
# In your views.py or wherever you use the agent:

user_input = "Open Chrome with KHAYALICO profile and go to LinkedIn"
# Agent will automatically use computer_control tool
# You'll SEE the actions happening!
```

---

## 🎨 Visual Feedback

### What You'll See

1. **Windows Key Opens**
   - Start menu appears

2. **Typing Happens**
   - You see characters being typed

3. **Applications Launch**
   - Chrome/Calculator/Notepad opens

4. **Mouse Moves & Clicks**
   - Cursor moves to target
   - Clicks happen visually

5. **Text Entry**
   - See typing in real-time

6. **Screenshots Saved**
   - Visual proof of completion

---

## ⚙️ Configuration

### Adjust Speed
```python
# In tools.py, modify ComputerController class:
self.action_delay = 0.5  # Seconds between actions

# Or use pyautogui settings:
pyautogui.PAUSE = 0.5  # Global pause
```

### Disable Safety
```python
# NOT RECOMMENDED, but if needed:
pyautogui.FAILSAFE = False  # Disables mouse corner failsafe
```

---

## 🔍 Supported Actions

| Action Type | Keywords | Example |
|------------|----------|---------|
| **Open** | open, launch, start, run | "open chrome" |
| **Click** | click, press, tap, select | "click on profile" |
| **Type** | type, write, enter, input | "type 'hello'" |
| **Navigate** | navigate, go to, visit | "navigate to linkedin.com" |
| **Search** | search, find, look for | "search for python" |
| **Scroll** | scroll, move down, move up | "scroll down" |
| **Switch** | switch, change, move to | "switch to KHAYALICO" |
| **Wait** | wait, pause, delay | "wait 2 seconds" |
| **Keys** | press enter, ctrl+c, etc | "press enter" |

---

## 🎯 Best Practices

### ✅ Do's
- Use clear, simple language
- Break complex tasks into steps with "then"
- Verify applications are visible on screen
- Use FAILSAFE (mouse to corner) if needed
- Check screenshots for verification

### ❌ Don'ts
- Don't use overly complex single commands
- Don't expect instant execution (actions take time)
- Don't move mouse manually during execution
- Don't minimize target applications
- Don't use on unsaved work (save first!)

---

## 🐛 Troubleshooting

### Issue: "Could not find element"
**Solution:** Make sure the target application is visible and not minimized

### Issue: "Actions too fast"
**Solution:** Increase `action_delay` in ComputerController class

### Issue: "Wrong window clicked"
**Solution:** Make target window active before running command

### Issue: "Tool stopped mid-execution"
**Solution:** Mouse touched top-left corner (FAILSAFE). Restart.

---

## 🌐 Platform Support

### Windows ✅
- Full support
- Uses Windows key for app launcher
- Native keyboard shortcuts

### macOS 🔶
- Supported (needs testing)
- Uses Spotlight for app launcher
- CMD key instead of Ctrl

### Linux 🔶
- Supported (needs testing)
- Uses application menu
- Various desktop environments

---

## 🎉 Summary

You now have a **universal computer control tool** that:

1. ✅ Takes natural language prompts
2. ✅ Breaks them into executable steps
3. ✅ Performs actions VISUALLY on your screen
4. ✅ Works with ANY application
5. ✅ Provides real-time feedback
6. ✅ Saves screenshots for verification

### No More Hard-Coding!

**Before:**
```python
def open_chrome_profile():
    # 50 lines of hard-coded logic
```

**Now:**
```python
computer_control("open chrome with KHAYALICO profile")
# DONE! And you SEE it happen!
```

---

## 📞 Support

For issues or questions:
1. Check the screenshots (current_screen.png, screen_info.png)
2. Review error messages in return values
3. Test with simple commands first
4. Verify all packages are installed

---

**Happy Automating! 🤖✨**
