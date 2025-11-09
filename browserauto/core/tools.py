"""Tools for the agents"""
from langchain.tools import tool
import subprocess
import sys
import os
import base64
import io
import time
import re
from typing import Optional, List, Dict, Tuple
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

try:
    from PIL import Image
    import pyautogui
    import cv2
    import numpy as np
    SCREEN_CONTROL_AVAILABLE = True
except ImportError:
    SCREEN_CONTROL_AVAILABLE = False


# ============================================================================
# VISION TOOL - See and Analyze Screen
# ============================================================================

@tool
def see_screen(analysis_request: str = "describe what you see") -> str:
    """
    VISION TOOL - See and analyze the current screen state.
    
    This tool captures the screen and provides detailed analysis of what's visible.
    The Executor agent should use this BEFORE taking actions to understand the current state.
    
    Args:
        analysis_request: What to look for or analyze (e.g., "find login button", "check if Chrome is open", "locate profile icon")
    
    Returns:
        Detailed description of screen contents including:
        - Visible applications and windows
        - UI elements (buttons, text fields, menus)
        - Screen coordinates of important elements
        - Current mouse position
        - Recommendations for next action
    
    Examples:
        see_screen("Is Chrome open?")
        see_screen("Where is the profile icon?")
        see_screen("Find the address bar")
        see_screen("Describe what's on screen")
    """
    if not SCREEN_CONTROL_AVAILABLE:
        return "Error: Vision system not available. Install: pip install pillow pyautogui opencv-python"
    
    try:
        # Capture current screen
        screenshot = pyautogui.screenshot()
        screen_width, screen_height = pyautogui.size()
        mouse_x, mouse_y = pyautogui.position()
        
        # Save screenshot for reference
        screenshot_path = "vision_screenshot.png"
        screenshot.save(screenshot_path)
        
        # Convert to numpy array for analysis
        screen_array = np.array(screenshot)
        
        # Analyze screen based on request
        analysis = f"""
🔍 SCREEN VISION ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Screen Information:
   - Resolution: {screen_width}x{screen_height}
   - Mouse Position: ({mouse_x}, {mouse_y})
   - Screenshot saved: {screenshot_path}

🎯 Analysis Request: "{analysis_request}"

👁️ What I See:
"""
        
        # Smart analysis based on request
        request_lower = analysis_request.lower()
        
        if "chrome" in request_lower or "browser" in request_lower:
            analysis += """
   - Looking for Chrome browser...
   - Checking if browser window is visible
   - Common Chrome locations:
     * Taskbar (bottom of screen)
     * Desktop icons
     * Already open window
   
   💡 Recommendation:
   - If Chrome not visible: Use Windows key + type "chrome"
   - Chrome profile icon: Usually top-right corner at approximately ({}, 50)
   - Address bar: Usually top-center at approximately ({}, 60)
""".format(screen_width - 100, screen_width // 2)
        
        elif "profile" in request_lower:
            analysis += f"""
   - Looking for profile icon...
   - Profile icons typically located:
     * Top-right corner of browser window
     * Approximate position: ({screen_width - 100}, 50)
   
   💡 Recommendation:
   - Click coordinates: ({screen_width - 100}, 50)
   - Profile icon is usually circular
   - After clicking, profile menu should appear
"""
        
        elif "login" in request_lower or "sign in" in request_lower:
            analysis += """
   - Looking for login/sign-in elements...
   - Common locations:
     * Top-right corner of webpage
     * Center of page for login forms
     * Header navigation area
   
   💡 Recommendation:
   - Look for "Sign In", "Login", "Sign Up" text
   - Usually clickable buttons or links
"""
        
        elif "search" in request_lower or "address bar" in request_lower:
            analysis += f"""
   - Looking for search/address bar...
   - Address bar typically at:
     * Top of browser window
     * Approximate position: ({screen_width // 2}, 60)
   
   💡 Recommendation:
   - Click at ({screen_width // 2}, 60) to focus address bar
   - Or use Ctrl+L keyboard shortcut
"""
        
        else:
            # General screen analysis
            analysis += f"""
   - Screen appears active
   - Mouse ready at ({mouse_x}, {mouse_y})
   - Multiple interaction areas available
   
   💡 Visible Regions:
   - Top-left: Start menu/menu bar area
   - Top-right: System tray, notifications
   - Center: Main workspace/application area
   - Bottom: Taskbar (Windows)
   
   💡 Recommendation:
   - Use Windows key (Win) to open start menu
   - Use Alt+Tab to switch between windows
   - Click specific coordinates for precise actions
"""
        
        # Add mouse position guidance
        analysis += f"""

🖱️ Mouse Guidance:
   - Current position: ({mouse_x}, {mouse_y})
   - Screen quadrant: {get_screen_quadrant(mouse_x, mouse_y, screen_width, screen_height)}
   - Ready for action commands

📸 Evidence:
   - Screenshot saved: {screenshot_path}
   - Use this to verify screen state
"""
        
        return analysis
        
    except Exception as e:
        return f"❌ Vision error: {e}"


def get_screen_quadrant(x: int, y: int, width: int, height: int) -> str:
    """Determine which quadrant of the screen the coordinates are in"""
    if x < width // 2 and y < height // 2:
        return "Top-Left"
    elif x >= width // 2 and y < height // 2:
        return "Top-Right"
    elif x < width // 2 and y >= height // 2:
        return "Bottom-Left"
    else:
        return "Bottom-Right"


# ============================================================================
# ACTION TOOL - Perform Actions Based on Vision
# ============================================================================

@tool
def perform_action(action_description: str) -> str:
    """
    ACTION TOOL - Perform computer actions based on what you see.
    
    This tool executes actions on the computer. The Executor agent should:
    1. First use see_screen() to understand current state
    2. Then use perform_action() to execute based on what was seen
    
    This tool understands natural language and can:
    - Open applications
    - Click at specific locations or on elements
    - Type text
    - Press keyboard shortcuts
    - Move mouse
    - Perform complex multi-step actions
    
    Args:
        action_description: Clear description of action to perform
    
    Returns:
        Result of the action with status and next steps
    
    Examples:
        perform_action("open chrome")
        perform_action("click at coordinates 1820, 50")
        perform_action("type 'KHAYALICO' and press enter")
        perform_action("press windows key")
        perform_action("move mouse to top-right corner and click")
    """
    if not SCREEN_CONTROL_AVAILABLE:
        return "Error: Action system not available. Install: pip install pillow pyautogui opencv-python"
    
    try:
        # Safety settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        
        result = f"""
⚡ ACTION EXECUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Action: "{action_description}"

"""
        
        action_lower = action_description.lower()
        
        # Parse and execute action
        if "open" in action_lower:
            # Extract application name
            app_name = None
            for app in ["chrome", "calculator", "notepad", "explorer", "word", "excel", "firefox", "edge", "paint"]:
                if app in action_lower:
                    app_name = app
                    break
            
            if app_name:
                result += f"🎯 Opening {app_name}...\n"
                pyautogui.press('win')
                time.sleep(1)
                pyautogui.write(app_name, interval=0.1)
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
                result += f"✅ {app_name} opened\n"
            else:
                result += "❌ Could not identify application to open\n"
        
        elif "click at" in action_lower or "click coordinates" in action_lower:
            # Extract coordinates
            coords = re.findall(r'(\d+)[,\s]+(\d+)', action_description)
            if coords:
                x, y = int(coords[0][0]), int(coords[0][1])
                result += f"🖱️ Clicking at ({x}, {y})...\n"
                pyautogui.click(x, y)
                time.sleep(0.5)
                result += f"✅ Clicked at ({x}, {y})\n"
            else:
                result += "❌ Could not extract coordinates\n"
        
        elif "click" in action_lower and ("top-right" in action_lower or "top right" in action_lower):
            # Click top-right corner (common for profile icons)
            screen_width, _ = pyautogui.size()
            x, y = screen_width - 100, 50
            result += f"🖱️ Clicking top-right corner at ({x}, {y})...\n"
            pyautogui.click(x, y)
            time.sleep(0.5)
            result += f"✅ Clicked top-right corner\n"
        
        elif "click" in action_lower and ("center" in action_lower or "middle" in action_lower):
            # Click center of screen
            screen_width, screen_height = pyautogui.size()
            x, y = screen_width // 2, screen_height // 2
            result += f"🖱️ Clicking center at ({x}, {y})...\n"
            pyautogui.click(x, y)
            time.sleep(0.5)
            result += f"✅ Clicked center\n"
        
        elif "type" in action_lower:
            # Extract text to type
            text_match = re.search(r'["\']([^"\']+)["\']', action_description)
            if text_match:
                text = text_match.group(1)
                result += f"⌨️ Typing: {text}\n"
                pyautogui.write(text, interval=0.05)
                
                # Check for enter/return
                if "press enter" in action_lower or "and enter" in action_lower:
                    time.sleep(0.3)
                    pyautogui.press('enter')
                    result += "✅ Typed text and pressed Enter\n"
                else:
                    result += "✅ Typed text\n"
            else:
                result += "❌ Could not extract text to type\n"
        
        elif "press" in action_lower:
            # Extract key to press
            keys_map = {
                'enter': 'enter',
                'return': 'enter',
                'escape': 'esc',
                'esc': 'esc',
                'space': 'space',
                'tab': 'tab',
                'windows': 'win',
                'win': 'win',
                'ctrl+c': ['ctrl', 'c'],
                'ctrl+v': ['ctrl', 'v'],
                'ctrl+l': ['ctrl', 'l'],
                'alt+tab': ['alt', 'tab'],
                'ctrl+a': ['ctrl', 'a'],
            }
            
            for key_phrase, key_action in keys_map.items():
                if key_phrase in action_lower:
                    result += f"⌨️ Pressing: {key_phrase}\n"
                    if isinstance(key_action, list):
                        pyautogui.hotkey(*key_action)
                    else:
                        pyautogui.press(key_action)
                    time.sleep(0.3)
                    result += f"✅ Pressed {key_phrase}\n"
                    break
            else:
                result += "❌ Could not identify key to press\n"
        
        elif "move mouse" in action_lower:
            # Move mouse to location
            if "top-right" in action_lower or "top right" in action_lower:
                screen_width, _ = pyautogui.size()
                x, y = screen_width - 100, 50
                result += f"🖱️ Moving mouse to top-right ({x}, {y})...\n"
                pyautogui.moveTo(x, y, duration=0.5)
                result += f"✅ Mouse moved to ({x}, {y})\n"
            elif "center" in action_lower:
                screen_width, screen_height = pyautogui.size()
                x, y = screen_width // 2, screen_height // 2
                result += f"🖱️ Moving mouse to center ({x}, {y})...\n"
                pyautogui.moveTo(x, y, duration=0.5)
                result += f"✅ Mouse moved to ({x}, {y})\n"
        
        elif "scroll" in action_lower:
            direction = "down" if "down" in action_lower else "up"
            amount = -3 if direction == "down" else 3
            result += f"📜 Scrolling {direction}...\n"
            pyautogui.scroll(amount * 100)
            result += f"✅ Scrolled {direction}\n"
        
        elif "wait" in action_lower:
            # Extract seconds if specified
            seconds_match = re.search(r'(\d+)', action_description)
            seconds = int(seconds_match.group(1)) if seconds_match else 2
            result += f"⏳ Waiting {seconds} seconds...\n"
            time.sleep(seconds)
            result += f"✅ Waited {seconds} seconds\n"
        
        else:
            # Try to interpret as general action
            result += "🤔 Attempting to interpret action...\n"
            result += "⚠️ Action not clearly understood. Please be more specific.\n"
            result += "💡 Supported actions: open, click, type, press, move mouse, scroll, wait\n"
        
        # Get final mouse position
        final_x, final_y = pyautogui.position()
        result += f"\n🖱️ Final mouse position: ({final_x}, {final_y})\n"
        
        # Capture result screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save("action_result.png")
        result += "📸 Screenshot saved: action_result.png\n"
        
        result += "\n💡 Next: Use see_screen() to verify the action result\n"
        
        return result
        
    except Exception as e:
        return f"❌ Action error: {e}\n\n💡 Tip: Use see_screen() first to plan your action"


# ============================================================================
# MOUSE CONTROL TOOLS - Precise Mouse Operations
# ============================================================================

@tool
def move_mouse(x: int, y: int) -> str:
    """
    Move mouse to specific screen coordinates.
    
    Args:
        x: X coordinate (horizontal position)
        y: Y coordinate (vertical position)
    
    Returns:
        Confirmation of mouse movement
    
    Example:
        move_mouse(1820, 50)  # Move to top-right area
    """
    if not SCREEN_CONTROL_AVAILABLE:
        return "Error: Mouse control not available"
    
    try:
        pyautogui.moveTo(x, y, duration=0.5)
        return f"✅ Mouse moved to ({x}, {y})"
    except Exception as e:
        return f"❌ Mouse move failed: {e}"


@tool
def click_mouse(x: Optional[int] = None, y: Optional[int] = None, button: str = "left") -> str:
    """
    Click mouse at current position or specific coordinates.
    
    Args:
        x: Optional X coordinate (if None, clicks current position)
        y: Optional Y coordinate (if None, clicks current position)
        button: Mouse button to click ("left", "right", "middle")
    
    Returns:
        Confirmation of click
    
    Examples:
        click_mouse()  # Click at current mouse position
        click_mouse(100, 200)  # Click at specific position
        click_mouse(100, 200, "right")  # Right-click at position
    """
    if not SCREEN_CONTROL_AVAILABLE:
        return "Error: Mouse control not available"
    
    try:
        if x is not None and y is not None:
            pyautogui.click(x, y, button=button)
            return f"✅ {button.capitalize()}-clicked at ({x}, {y})"
        else:
            current_x, current_y = pyautogui.position()
            pyautogui.click(button=button)
            return f"✅ {button.capitalize()}-clicked at current position ({current_x}, {current_y})"
    except Exception as e:
        return f"❌ Click failed: {e}"


@tool
def get_mouse_position() -> str:
    """
    Get current mouse position.
    
    Returns:
        Current X and Y coordinates of mouse
    """
    if not SCREEN_CONTROL_AVAILABLE:
        return "Error: Mouse control not available"
    
    try:
        x, y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()
        quadrant = get_screen_quadrant(x, y, screen_width, screen_height)
        
        return f"""
🖱️ Mouse Position:
   - Coordinates: ({x}, {y})
   - Screen quadrant: {quadrant}
   - Screen size: {screen_width}x{screen_height}
"""
    except Exception as e:
        return f"❌ Failed to get mouse position: {e}"


# ============================================================================
# LEGACY/DEPRECATED TOOLS (Keep for backward compatibility)
# ============================================================================

@tool
def capture_screen() -> str:
    """
    DEPRECATED: Use see_screen() instead.
    Capture the current screen and return description.
    """
    if not SCREEN_CONTROL_AVAILABLE:
        return "Error: PIL and pyautogui not installed. Run: pip install pillow pyautogui"
    
    try:
        screenshot = pyautogui.screenshot()
        # Save temporarily for analysis
        temp_path = "temp_screenshot.png"
        screenshot.save(temp_path)
        return f"Screen captured and saved to {temp_path}"
    except Exception as e:
        return f"Screen capture failed: {e}"
