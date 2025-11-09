"""
Test script to verify the agent setup
"""
import os
import sys
import django

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'browserauto.settings')
django.setup()

from core.agents import get_swarm_response

def test_agents():
    print("Testing Alice and Bob agents...\n")
    
    # Test 1: Initial greeting
    print("Test 1: Asking to speak to Bob")
    response1 = get_swarm_response("i'd like to speak to Bob", "test_thread")
    messages1 = response1.get('messages', [])
    last_msg1 = messages1[-1]
    print(f"Active Agent: {response1.get('active_agent')}")
    print(f"Response: {last_msg1.content}\n")
    
    # Test 2: Math question
    print("Test 2: Asking a math question")
    response2 = get_swarm_response("what's 5 + 7?", "test_thread")
    messages2 = response2.get('messages', [])
    last_msg2 = messages2[-1]
    print(f"Active Agent: {response2.get('active_agent')}")
    print(f"Response: {last_msg2.content}\n")
    
    print("Tests completed successfully!")

if __name__ == "__main__":
    test_agents()
