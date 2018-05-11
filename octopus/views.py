from django.shortcuts import render_to_response, render
from django.views import View
from django.views.generic import ListView

from octopus.models import Comment
from octopus.models.hypothesis import Hypothesis


class HypothesisListView(ListView):
    model = Hypothesis


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PrototypeView(View):
    def get(self, request):
        return render(
            request,
            'base_template.html',
            context={
                'comments' : Comment.objects.order_by('-id'),
                'hypotheses' : Hypothesis.objects.all()
            }
        )

class HypothesisCreate(CreateView):
    model = Hypothesis
    fields = ['name']


class HypothesisUpdate(UpdateView):
    model = Hypothesis
    fields = ['name']


class HypothesisDelete(DeleteView):
    model = Hypothesis
    success_url = reverse_lazy('hypothesis-list')
