from django.urls import path, include
from exam import views

app_name = "exam"

urlpatterns = [
    path('<str:pk>/start', views.take_test, name='take_test'),
    path('<str:pk>/new', views.QuestionCreate.as_view(), name='create_question'),
]