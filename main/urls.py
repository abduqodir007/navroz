from django.urls import path,include
from main import views
from .views import *

app_name = "main"

urlpatterns = [
    # diller
    path('diller/',Diller_View.as_view()),
    path('diller/<int:pk>/',Diller_Id.as_view()),
    path('diller/<int:pk>/',Diller_Delete.as_view()),
    path('diller/<int:pk>/',Diller_Update.as_view()),
    path('diller/create/',Diller_Create.as_view()),
    # product
    path('product/',Product_View.as_view()),
    path('product/<int:pk>/',Product_Id.as_view()),
    path('product/<int:pk>/',Product_Delete.as_view()),
    path('product/<int:pk>/',Product_Update.as_view()),
    path('product/create/',Product_Create.as_view()),
]