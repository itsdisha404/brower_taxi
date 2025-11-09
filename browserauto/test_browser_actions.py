"""Test the new browser action tools"""
import os
import sys
from dotenv import load_dotenv

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.tools import browser_action, get_page_content, capture_screen

def test_browser_actions():
    """Test browser automation with natural language prompts"""
    
    print("=" * 60)
    print("Testing Browser Action Tools")
    print("=" * 60)
    
    # Test 1: Navigate to LinkedIn
    print("\n1. Navigating to LinkedIn...")
    result = browser_action("navigate to https://www.linkedin.com")
    print(f"Result: {result}")
    
    # Wait a bit for page to load
    import time
    time.sleep(3)
    
    # Test 2: Get page content
    print("\n2. Getting page content...")
    result = get_page_content()
    print(f"Result: {result[:200]}...")
    
    # Test 3: Take screenshot
    print("\n3. Taking screenshot...")
    result = capture_screen()
    print(f"Result: {result}")
    
    # Test 4: Scroll down
    print("\n4. Scrolling down the page...")
    result = browser_action("scroll down")
    print(f"Result: {result}")
    
    time.sleep(2)
    
    # Test 5: Close browser
    print("\n5. Closing browser...")
    result = browser_action("close browser")
    print(f"Result: {result}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    load_dotenv()
    test_browser_actions()
