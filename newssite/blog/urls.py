from django.urls import path, include
from . import views
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name = "home")
]