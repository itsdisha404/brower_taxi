# Browser Automation Tools - Prompt-Based Actions

## Overview
Your tools now have the ability to view screens and take actions based on natural language prompts instead of hard-coded behavior!

## New Tools Added

### 1. `browser_action(action_prompt, url=None)`
**Main tool for browser automation via natural language**

Execute browser actions using simple prompts:

**Examples:**
```python
# Navigation
browser_action("navigate to https://linkedin.com")

# Clicking elements
browser_action("click on the sign in button")
browser_action("click on profile")

# Typing and form interaction
browser_action("type 'software engineer' in search box")
browser_action("type 'hello@example.com' and press enter")

# Scrolling
browser_action("scroll down")
browser_action("scroll up")

# Screenshots
browser_action("take a screenshot")

# Closing
browser_action("close browser")
```

**Features:**
- Automatically uses KHAYALICO Chrome profile
- Maintains browser session across multiple actions
- Smart element detection based on text content
- XPath-based element finding

### 2. `get_page_content()`
**Get current page information**

Returns:
- Page title
- Current URL
- Preview of page text content (first 1000 characters)

### 3. `capture_screen()`
**Take a screenshot of the entire screen**

Captures the current screen and saves to `temp_screenshot.png`

## How It Works

### Browser Session Management
- First call to `browser_action()` initializes a Chrome browser with your KHAYALICO profile
- The browser stays open between actions (persistent session)
- All subsequent calls reuse the same browser instance
- Call `browser_action("close browser")` to quit

### Natural Language Processing
The tool intelligently parses your prompts:

1. **Navigation**: Detects "navigate", "go to" + URL
2. **Clicking**: Finds elements containing specified text
3. **Typing**: Extracts quoted text and enters it into active input fields
4. **Scrolling**: Detects direction (up/down)
5. **Screenshots**: Captures current browser state

### Element Detection
When you say "click on login button", the tool:
1. Searches for elements containing the word "login"
2. Waits up to 5 seconds for element to be clickable
3. Clicks the element once found
4. Returns success/failure message

## Integration with Agent

The Alice agent now has access to all browser automation tools:

```python
# In agents.py
alice = create_react_agent(
    model,
    [
        open_chrome,          # Opens Chrome with profile + LinkedIn
        browser_action,       # Main prompt-based automation
        capture_screen,       # Screen capture
        get_page_content,     # Page content extraction
        create_handoff_tool(agent_name="Bob")
    ],
    prompt=ALICE_PROMPT,
    name="Alice",
)
```

## Usage Example

```python
from core.tools import browser_action, get_page_content

# Start browser and navigate
browser_action("navigate to https://www.linkedin.com")

# Check what's on the page
content = get_page_content()
print(content)

# Interact with page
browser_action("click on sign in")
browser_action("type 'myemail@example.com' in email field")
browser_action("scroll down")

# Close when done
browser_action("close browser")
```

## Testing

Run the test script to see it in action:

```bash
cd d:\tp_project\browserauto
python test_browser_actions.py
```

## Dependencies

All required packages are now installed:
- `selenium` - Browser automation
- `pillow` - Image processing
- `pyautogui` - Screen capture

## Advantages Over Hard-Coding

### Before (Hard-coded):
```python
def open_linkedin():
    subprocess.Popen([chrome_path, "--profile=KHAYALICO", "https://linkedin.com"])
```

### Now (Prompt-based):
```python
browser_action("open linkedin and click on jobs")
browser_action("search for 'python developer'")
browser_action("apply to the first job")
```

**Benefits:**
- ✅ Flexible and adaptable
- ✅ No code changes needed for new actions
- ✅ Natural language interface
- ✅ AI agent can control the browser dynamically
- ✅ Easy to extend and modify behavior

## Future Enhancements

Potential additions:
- Visual element detection using computer vision
- AI-powered page understanding
- Form auto-fill capabilities
- Multi-tab management
- Cookie and session handling
- Wait conditions and smart delays

## Notes

- The browser uses your existing KHAYALICO Chrome profile, so it will have your saved logins and cookies
- Make sure Chrome is installed in the default location
- The browser window will be maximized on start
- Screenshots are saved as `temp_screenshot.png` in the current directory
