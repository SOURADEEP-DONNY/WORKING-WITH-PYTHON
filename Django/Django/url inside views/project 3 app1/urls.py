#FOR APP1
from django.urls import path
from app1 import views
urlpatterns = [
    path('learndj1/', views.learn_django),
    path('learnpy1/', views.learn_python),
]
