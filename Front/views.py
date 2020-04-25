from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from .forms import *
import requests
import json

#BASE_URL = "http://127.0.0.1:8000/"
BASE_URL = "https://kartia.herokuapp.com/"
HEADERS = {'Content-type': 'application/json'}

class Login(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def form_valid(self, form):
        data = {
            "username" : form.cleaned_data["username"],
            "password" : form.cleaned_data["password"]
        }

        
        response = requests.post(BASE_URL+"token-auth/login/", json=data, headers=HEADERS)
        result = json.loads(response.content.decode("utf-8"))
        if "token" in result:
            self.request.session["Token"] = "token " + str(result["token"])
            return redirect(reverse("front:home"))
        else:
            return self.form_invalid(form)

class CarPanel(TemplateView):
    template_name = "panel.html"

    def get_context_data(self, **kwargs):
        context = super(CarPanel, self).get_context_data(**kwargs)
        context["base_url"] = BASE_URL
        context["token"] = self.request.session["Token"]
        return context

# Create your views here.
