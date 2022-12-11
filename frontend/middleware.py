from ipware import get_client_ip
from .models import Visitor
import time
class VisitorsIp:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self,request):
        ip, is_routable = get_client_ip(request)
        v = Visitor(ip=ip, visit_at = time.localtime())
        v.save()
        response = self.get_response(request)
        return response
