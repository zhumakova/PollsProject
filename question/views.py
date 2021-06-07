from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from .services import *


def question_page(request,poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        return HttpResponse('404')
    questions = poll.question_set.all()
    answer_formset = formset_factory(AnswerForm,extra=len(questions))
    form = answer_formset()
    if request.method == 'POST':
        form = answer_formset(request.POST)
        if form.is_valid():
            points = check_answer(questions,form.cleaned_data)
            UserToPoll.objects.create(user=request.user,poll=poll,points=points)
            return HttpResponse('Thank you!')
    return render(request,'question.html',{'questions':questions,'form':form})
