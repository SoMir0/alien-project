from django.contrib import admin
from django.urls import path, include

from alienproject.spa.views import SpaView
from alienproject.api.views import GreetingApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/greet", GreetingApi.as_view()),  # <-- here
    path('', SpaView.as_view(), name="spa"),
]
