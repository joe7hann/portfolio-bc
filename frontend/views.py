from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import urllib.request
import json
import datetime

from django.http import HttpResponse


class FrontEndView(View):
    def get(self, request):
        return render(request, "index.html")
