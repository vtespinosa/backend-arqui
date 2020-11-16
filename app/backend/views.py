from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User, Room, Message
# from .helpers.aws_helper import LambdaConnect
from .serializers import RoomSerializer, MessageSerializer
from rest_framework import generics
import json
from functools import wraps
import jwt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

def create_user(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)
    nickname = body['nickname']
    email = body['mail']
    user = User(nickname=nickname)
    user.save()
    data = {"payload": {"email": email, "msg": nickname}}
    data["function_name"] = "send_email"
    # lambda_connect = LambdaConnect()
    # lambda_connect.lambda_invoker(**data)
    return HttpResponse(json.dumps({'success': True}))


def create_room(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)
    try:
        name = body['name']
        room = Room(name=name)
        room.save()
        return HttpResponse(json.dumps({'success': True}))
    except:
        return HttpResponse(json.dumps({'success': False}), status=400)

@permission_classes([AllowAny])
def check_health(request):
    return JsonResponse({'success': True}, status=200)


# Sends list of all rooms to frontend
class rooms(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Sends list of all messages to frontend
class messages(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
