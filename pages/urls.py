from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutUsPage.as_view(), name='about'  ),
    path('test/', test, name='test'),
]