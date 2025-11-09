"""Test the universal computer control tool"""
import os
import sys
from dotenv import load_dotenv

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.tools import computer_control, get_screen_info

def test_computer_control():
    """Test universal computer control with various prompts"""
    
    print("=" * 80)
    print("UNIVERSAL COMPUTER CONTROL - TEST SUITE")
    print("=" * 80)
    print("\n⚠️  WARNING: The tool will control your mouse and keyboard!")
    print("Move your mouse to the top-left corner of the screen to stop (FAILSAFE)")
    print("\nStarting in 3 seconds...")
    
    import time
    time.sleep(3)
    
    # Test scenarios
    tests = [
        {
            'name': 'Test 1: Open Chrome with KHAYALICO Profile',
            'prompt': 'Open Chrome, then click on profile icon, then select KHAYALICO'
        },
        {
            'name': 'Test 2: Open Calculator',
            'prompt': 'Open calculator'
        },
        {
            'name': 'Test 3: Open Notepad and Type',
            'prompt': 'Open notepad, then type "Hello from AI Agent"'
        },
        {
            'name': 'Test 4: Chrome + LinkedIn Navigation',
            'prompt': 'Open chrome, switch to KHAYALICO profile, then navigate to linkedin.com'
        },
    ]
    
    # Run selected test (change this number to run different tests)
    test_to_run = 1  # Change to 0, 1, 2, or 3
    
    test = tests[test_to_run]
    print(f"\n{'='*80}")
    print(f"🧪 {test['name']}")
    print(f"📝 Prompt: {test['prompt']}")
    print(f"{'='*80}\n")
    
    result = computer_control(test['prompt'])
    
    print(f"\n{'='*80}")
    print("RESULT:")
    print(f"{'='*80}")
    print(result)
    print(f"{'='*80}\n")
    
    # Get final screen info
    print("\n📊 Final Screen State:")
    screen_info = get_screen_info()
    print(screen_info)
    
    print("\n" + "=" * 80)
    print("✅ TEST COMPLETED!")
    print("=" * 80)


def demo_simple_actions():
    """Demo simple individual actions"""
    print("\n" + "=" * 80)
    print("SIMPLE ACTIONS DEMO")
    print("=" * 80)
    
    import time
    
    # Demo 1: Get screen info
    print("\n1️⃣  Getting screen information...")
    result = get_screen_info()
    print(result)
    
    time.sleep(2)
    
    # Demo 2: Simple open
    print("\n2️⃣  Opening calculator...")
    result = computer_control("open calculator")
    print(result)
    
    time.sleep(3)
    
    # Demo 3: Type in calculator
    print("\n3️⃣  Typing in calculator...")
    result = computer_control("type 123")
    print(result)
    
    print("\n" + "=" * 80)
    print("✅ DEMO COMPLETED!")
    print("=" * 80)


if __name__ == "__main__":
    load_dotenv()
    
    print("\n" + "=" * 80)
    print("SELECT TEST MODE:")
    print("=" * 80)
    print("1. Run full computer control test")
    print("2. Run simple actions demo")
    print("=" * 80)
    
    # Run full test (comment out to run demo instead)
    test_computer_control()
    
    # Or run simple demo (uncomment to run)
    # demo_simple_actions()
