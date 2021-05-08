#APP2 URLS
from django.urls import path
from app2 import views
urlpatterns = [
    path('app2learndj/', views.learn2_django),
    path('app2learnpy/', views.learn2_python)
]
