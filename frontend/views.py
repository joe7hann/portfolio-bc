from django.shortcuts import render, redirect
from .models import Project, Visitor
from .forms import NewProjectForm
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse


# class FrontEndView(TemplateView):
#     template_name =  "index.html"
#     extra_context =  {"projects":Project.objects.all()}

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["projects"] = Project.objects.all()
#         return context


class FrontEndView(ListView):
    model = Project
    template_name = "index.html"

    


class VisitorsView(LoginRequiredMixin,ListView):
    model = Visitor
    template_name = "visitors.html"
    paginate_by = 9


class RegisterNewProjectView(LoginRequiredMixin,FormView):
    model = Project
    template_name = "create_new_project.html"
    form_class = NewProjectForm

    def form_valid(self, form):
        #print(form.cleaned_data['name'])
        Project.objects.create(**form.cleaned_data)
        return redirect("index") #
