from typing import Any
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/question_list.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the recently published 5 questions
        excluding those published in the future."""
        # return Question.objects.order_by("-pub_date")[:5]
    
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"
    def get_queryset(self):
        """previously returned the questions in future too if the right url is provided.
        This function ensures to show only published questions. """
        return Question.objects.filter(pub_date__lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/question_results.html"
    def get_queryset(self):
        """previously returned the questions in future too if the right url is provided.
        This function ensures to show only published questions. """
        return Question.objects.filter(pub_date__lte = timezone.now())

def vote(request,pk):
    question = get_object_or_404(Question, pk = pk)
    context = {
        "question" : question,
        "error_message" : "Please select a choice."
    }
    try:
        ## request.POST is a dictionary like object that help to retrieve the data using the key as choice
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponse(f"You have successfully voted {selected_choice.choice_text} in the question of id : {question.id} of\n{question}.")
        # return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        return redirect("polls:results",pk = question.id)
