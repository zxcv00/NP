from django.urls import path
from playground import views

app_name = 'playground'

urlpatterns = [
    path('bye/', views.say_bye, name='bye'),  # playground: hello
    path('bye_html/', views.say_bye_html, name='bye_html'),
]