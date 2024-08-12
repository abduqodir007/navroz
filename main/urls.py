from django.urls import path,include
from main import views
from .views import *

app_name = "main"

urlpatterns = [
    path('',ListApiView2.as_view()),
    path('<int:pk>/',Id.as_view()),
    path('<int:pk>/delete/',Delete.as_view()),
    path('<int:pk>/update/',Update.as_view()),
    path('create/',Create.as_view()),
]