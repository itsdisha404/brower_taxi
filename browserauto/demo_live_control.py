"""
DEMO: Open Chrome with KHAYALICO Profile and Navigate to LinkedIn

This script demonstrates the universal computer control tool with your exact use case.
You will SEE the actions happening on your screen!
"""

import os
import sys
from dotenv import load_dotenv
import time

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.tools import computer_control, get_screen_info

def main():
    """Run the KHAYALICO Chrome + LinkedIn demo"""
    
    print("=" * 80)
    print("🎬 UNIVERSAL COMPUTER CONTROL - LIVE DEMO")
    print("=" * 80)
    print()
    print("📋 Task: Open Chrome with KHAYALICO profile and go to LinkedIn")
    print()
    print("⚠️  WARNING:")
    print("   - Your mouse and keyboard will be controlled by AI")
    print("   - DO NOT touch your mouse or keyboard during execution")
    print("   - Move mouse to TOP-LEFT corner to emergency stop")
    print("   - Save any unsaved work before proceeding")
    print()
    print("=" * 80)
    
    # Countdown
    print("\n⏳ Starting in:")
    for i in range(5, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    print("\n🚀 EXECUTING NOW - WATCH YOUR SCREEN!\n")
    print("=" * 80)
    
    # THE MAGIC HAPPENS HERE
    result = computer_control(
        "open chrome, then click on profile icon, then select KHAYALICO, then navigate to linkedin.com"
    )
    
    print("\n" + "=" * 80)
    print("📊 EXECUTION RESULTS:")
    print("=" * 80)
    print(result)
    print("=" * 80)
    
    # Get final screen state
    print("\n📸 Capturing final screen state...")
    screen_info = get_screen_info()
    print(screen_info)
    
    print("\n" + "=" * 80)
    print("✅ DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print("\n📁 Check these files:")
    print("   - current_screen.png (final state)")
    print("   - screen_info.png (screen capture)")
    print("\n🎉 Your AI agent can now control your computer!")
    print("=" * 80)


def test_simple():
    """Test with a simpler action first"""
    
    print("=" * 80)
    print("🧪 SIMPLE TEST - Open Calculator")
    print("=" * 80)
    print("\nStarting in 3 seconds...")
    time.sleep(3)
    
    result = computer_control("open calculator")
    
    print("\n" + "=" * 80)
    print("RESULT:")
    print("=" * 80)
    print(result)
    print("=" * 80)


if __name__ == "__main__":
    load_dotenv()
    
    print("\n" + "=" * 80)
    print("SELECT DEMO:")
    print("=" * 80)
    print("1. Full Demo: Chrome + KHAYALICO + LinkedIn (RECOMMENDED)")
    print("2. Simple Test: Just open Calculator")
    print("=" * 80)
    
    choice = input("\nEnter choice (1 or 2, default=1): ").strip() or "1"
    
    if choice == "2":
        test_simple()
    else:
        main()
