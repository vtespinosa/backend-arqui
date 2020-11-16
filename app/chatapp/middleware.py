import requests

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
        response = self.get_response(request)
        response['X-Instance-Id'] = x.text
        return response