from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
class HomePage(TemplateView):
    template_name = 'home.html'
    

class AboutUsPage(TemplateView):
    template_name = 'pages/about.html'

def test (request):
    result = 'hello world'
    messages.success(request, 'success')
    return render(request, 'pages/test.html')

