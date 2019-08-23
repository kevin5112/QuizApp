from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Exam, Question, Answer

def IndexView(request):
	template_name = 'quiz/index.html'
	return render(request, template_name)


class ExamView(generic.ListView):
	template_name = 'quiz/exam.html'
	context_object_name = 'exam_list'

	def get_queryset(self):
		"""
		Returns all the exam topics
		"""
		return Exam.objects.all()


class QuestionView(generic.DetailView):
	model = Question
	template_name = 'quiz/question.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet
		"""
		return Question.objects.filter(is_published=True)








