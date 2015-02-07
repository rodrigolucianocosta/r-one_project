#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from atendimento.models import Paciente
# Create your views here.
def index(request):
	latest_question_list = Paciente.objects.order('NascimentoData')[:5]
	template = loader.get_template('atendimento/index.html')
	context = RequestContext(request, {
		'latest_question_list' : latest_question_list,
		})
	return HttpResponse(template.render(context))

def detail(request, question_id):
	return HttpResponse("you are looking at question %s." % question_id)

def results(request,question_id):
	response = "You are looking at the results of question_id  %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you are voting on question %s." % question_id)