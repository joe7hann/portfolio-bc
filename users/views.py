from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import NewUserForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RegisterView(CreateView):
    template_name= "registration/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        return redirect('login')

class AdminView(LoginRequiredMixin,View):
    template = "admin-index.html"
    def get(self,request):
        return render(request, self.template)