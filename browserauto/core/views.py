from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .agents import get_swarm_response


def index(request):
    """Render the main page"""
    return render(request, 'core/index.html')


@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    """
    API endpoint to chat with the swarm agents
    
    Request body:
    {
        "message": "user message",
        "thread_id": "optional thread id"
    }
    
    Response:
    {
        "success": true,
        "response": "agent response",
        "active_agent": "Alice or Bob",
        "messages": [...all messages in the conversation]
    }
    """
    try:
        data = json.loads(request.body)
        message = data.get('message', '')
        thread_id = data.get('thread_id', 'default')
        
        if not message:
            return JsonResponse({
                'success': False,
                'error': 'Message is required'
            }, status=400)
        
        # Get response from agents
        response = get_swarm_response(message, thread_id)
        
        # Extract the last AI message
        messages = response.get('messages', [])
        last_message = messages[-1] if messages else None
        agent_response = last_message.content if last_message else "No response"
        
        return JsonResponse({
            'success': True,
            'response': agent_response,
            'active_agent': response.get('active_agent', 'Unknown'),
            'messages': [
                {
                    'role': msg.type if hasattr(msg, 'type') else 'unknown',
                    'content': msg.content if hasattr(msg, 'content') else str(msg),
                    'name': msg.name if hasattr(msg, 'name') else None
                }
                for msg in messages
            ]
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
