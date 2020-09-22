from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print("persona")

urlpatterns = [
    path('persona/', DesdeApps),
]