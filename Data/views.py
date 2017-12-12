from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import *
from .models import *


# not used

def db(request):

    DNASeqs = DNASeq.objects.all()
    RNASeqs = RNASeq.objects.all()
    PeptideSeqs = PeptideSeq.objects.all()

    return render(request, 'db.html', {
        'DNASeqs': DNASeqs,
        'RNASeqs': RNASeqs,
        'PeptideSeqs': PeptideSeqs
    })


# not used

def dnaupload(request):

    return render(request, 'dnaupload.html')


class DNAView(TemplateView):
    template_name = 'data/dnaupload.html'

    def get(self, request):
        form = DNAForm()
        posts = DNASeq.objects.all()
        print(posts)
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = DNAForm(request.POST)
        if form.is_valid():
            _post = form.save(commit=False)
            _post.save()
            text = form.cleaned_data['name']
            form = DNAForm()
        posts = DNASeq.objects.all()
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)


class RNAView(TemplateView):
    template_name = 'data/rnaupload.html'

    def get(self, request):
        form = RNAForm()
        posts = RNASeq.objects.all()
        print(posts)
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = RNAForm(request.POST)
        if form.is_valid():
            _post = form.save(commit=False)
            _post.save()
            text = form.cleaned_data['name']
            form = RNAForm()
        posts = RNASeq.objects.all()
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)


class PeptideView(TemplateView):
    template_name = 'data/peptideupload.html'

    def get(self, request):
        form = PeptideForm()
        posts = PeptideSeq.objects.all()
        print(posts)
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = PeptideForm(request.POST)
        if form.is_valid():
            _post = form.save(commit=False)
            _post.save()
            text = form.cleaned_data['name']
            form = PeptideForm()
        posts = PeptideSeq.objects.all()
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)
