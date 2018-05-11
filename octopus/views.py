from django.shortcuts import render_to_response, render, redirect
from django.views import View
from django.views.generic import ListView

from octopus.models import Comment
from octopus.models.hypothesis import Hypothesis

from octopus.forms import CommentForm

class HypothesisListView(ListView):
    model = Hypothesis


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PrototypeView(View):
    def get(self, request):
        comment_form = CommentForm()
        return render(
            request,
            'base_template.html',
            context={
                'comments' : Comment.objects.order_by('-id'),
                'hypothesis' : Hypothesis.objects.first(),
                'comment_form' : comment_form
            }
        )

    def post(self, request):
        comment_form = CommentForm(request.POST)
        comment_form.save()
        return redirect('/')

class HypothesisCreate(CreateView):
    model = Hypothesis
    fields = ['name']


class HypothesisUpdate(UpdateView):
    model = Hypothesis
    fields = ['name']


class HypothesisDelete(DeleteView):
    model = Hypothesis
    success_url = reverse_lazy('hypothesis-list')
