from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print("departamento")

urlpatterns = [
    path('departamento/', DesdeApps),
]