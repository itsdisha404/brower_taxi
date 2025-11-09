"""
Test the upgraded multi-agent swarm system

This demonstrates how the agents work together:
1. Coordinator receives request
2. TaskPlanner creates TODO list
3. Executor performs actions
4. Reporter provides results
"""

import os
import sys
from dotenv import load_dotenv

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.agents import get_swarm_response, stream_swarm_response


def test_swarm_workflow():
    """Test the complete agent swarm workflow"""
    
    print("=" * 80)
    print("🤖 MULTI-AGENT SWARM SYSTEM - TEST")
    print("=" * 80)
    print()
    print("Agent Architecture:")
    print("  1. 📋 Coordinator - Receives requests, orchestrates workflow")
    print("  2. 🎯 TaskPlanner - Creates detailed execution plans")
    print("  3. ⚡ Executor - Executes computer control actions")
    print("  4. 📊 Reporter - Formats and reports results")
    print()
    print("=" * 80)
    
    # Test case: Your exact use case
    user_request = "Open Chrome in KHAYALICO profile and then open LinkedIn"
    
    print(f"\n💬 User Request:")
    print(f"   '{user_request}'")
    print()
    print("=" * 80)
    print("🔄 AGENT WORKFLOW - WATCH THE SWARM IN ACTION")
    print("=" * 80)
    print()
    
    # Execute with swarm
    thread_id = "test_thread_1"
    
    print("⏳ Processing (agents are collaborating)...\n")
    
    try:
        response = get_swarm_response(user_request, thread_id)
        
        print("\n" + "=" * 80)
        print("📋 COMPLETE AGENT INTERACTION LOG")
        print("=" * 80)
        
        # Display all messages
        messages = response.get("messages", [])
        
        current_agent = None
        for i, msg in enumerate(messages, 1):
            # Detect agent changes
            if hasattr(msg, 'name') and msg.name:
                if msg.name != current_agent:
                    current_agent = msg.name
                    agent_emoji = {
                        'Coordinator': '📋',
                        'TaskPlanner': '🎯',
                        'Executor': '⚡',
                        'Reporter': '📊'
                    }.get(current_agent, '🤖')
                    print(f"\n{'='*80}")
                    print(f"{agent_emoji} AGENT: {current_agent}")
                    print(f"{'='*80}")
            
            # Display message content
            content = msg.content if hasattr(msg, 'content') else str(msg)
            if content and len(content.strip()) > 0:
                print(f"\n{content}")
        
        print("\n" + "=" * 80)
        print("✅ WORKFLOW COMPLETED")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


def test_streaming_workflow():
    """Test streaming to see real-time agent collaboration"""
    
    print("=" * 80)
    print("🌊 STREAMING AGENT WORKFLOW - REAL-TIME VIEW")
    print("=" * 80)
    
    user_request = "Open calculator"
    
    print(f"\n💬 User Request: '{user_request}'")
    print("\n🔄 Streaming agent responses...\n")
    print("=" * 80)
    
    try:
        for chunk in stream_swarm_response(user_request, "stream_thread_1"):
            if chunk:
                print(f"📦 Chunk received: {chunk}")
                print("-" * 80)
        
        print("\n✅ STREAMING COMPLETED")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


def test_multiple_requests():
    """Test multiple sequential requests"""
    
    print("=" * 80)
    print("🔢 MULTIPLE REQUESTS TEST")
    print("=" * 80)
    
    requests = [
        "Open calculator",
        "Open notepad and type 'Hello from AI swarm'",
        "Open Chrome with KHAYALICO profile and go to LinkedIn"
    ]
    
    for i, request in enumerate(requests, 1):
        print(f"\n{'='*80}")
        print(f"🧪 Test {i}/{len(requests)}: {request}")
        print(f"{'='*80}")
        
        try:
            response = get_swarm_response(request, f"multi_thread_{i}")
            
            # Get final message
            messages = response.get("messages", [])
            if messages:
                final_message = messages[-1]
                content = final_message.content if hasattr(final_message, 'content') else str(final_message)
                print(f"\n✅ Result:\n{content}")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
        
        print()
    
    print("=" * 80)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 80)


def interactive_mode():
    """Interactive mode to test with custom prompts"""
    
    print("=" * 80)
    print("🎮 INTERACTIVE SWARM MODE")
    print("=" * 80)
    print()
    print("Enter your automation requests and watch the agent swarm work!")
    print("Type 'quit' or 'exit' to stop")
    print()
    print("Example requests:")
    print("  - Open Chrome in KHAYALICO profile")
    print("  - Open calculator and type 123")
    print("  - Open notepad, type Hello, and save")
    print("  - Go to Chrome, switch to KHAYALICO, navigate to linkedin.com")
    print()
    print("=" * 80)
    
    thread_id = "interactive_thread"
    request_count = 0
    
    while True:
        print()
        user_input = input("💬 Your request: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not user_input:
            continue
        
        request_count += 1
        print(f"\n⏳ Processing request #{request_count}...\n")
        
        try:
            response = get_swarm_response(user_input, thread_id)
            
            # Display final result
            messages = response.get("messages", [])
            if messages:
                print("\n" + "=" * 80)
                print("📊 RESULT")
                print("=" * 80)
                
                final_message = messages[-1]
                content = final_message.content if hasattr(final_message, 'content') else str(final_message)
                print(f"\n{content}")
                print("\n" + "=" * 80)
            
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    load_dotenv()
    
    print("\n" + "=" * 80)
    print("SELECT TEST MODE:")
    print("=" * 80)
    print("1. Full workflow test (recommended)")
    print("2. Streaming test (see real-time agent work)")
    print("3. Multiple requests test")
    print("4. Interactive mode (try your own prompts)")
    print("=" * 80)
    
    choice = input("\nEnter choice (1-4, default=1): ").strip() or "1"
    print()
    
    if choice == "1":
        test_swarm_workflow()
    elif choice == "2":
        test_streaming_workflow()
    elif choice == "3":
        test_multiple_requests()
    elif choice == "4":
        interactive_mode()
    else:
        print("Invalid choice, running default test...")
        test_swarm_workflow()
