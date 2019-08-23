from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
	path('', views.IndexView, name='index'),
	path('exams/', views.ExamView.as_view(), name='exam'),
	path('<int:pk>/', views.QuestionView.as_view(), name='question'),
]