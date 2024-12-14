from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

class MainPageView(View):
    def get(self, request):
        return render(request, "main/index.html")

    def post(self, request):
        pass