from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, RedirectView, DeleteView

from .models import New, Comment

from .forms import NewForm, VoteForm, CommentForm

# Create your views here.


class NewList(ListView):
    context_object_name = 'News'
    template_name = 'news/new_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = New.objects.all()
        query = self.request.GET.get('q', None)
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs


class NewAdd(CreateView):
    model = New
    form_class = NewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('New:list')


class NewEdit(UpdateView):
    model = New
    form_class = NewForm

    def get_success_url(self):
        return reverse_lazy('New:detail', args=(self.object.id, ))


class NewDelete(DeleteView):
    model = New
    success_url = reverse_lazy('New:list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return reverse_lazy('New:detail', kwargs={'pk': self.kwargs['pk']})
        else:
            return super(NewDelete, self).post(request, *args, **kwargs)


class NewDetail(DetailView):
    model = New


class NewVote(UpdateView):
    model = New
    form_class = VoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.vote:
            form.instance.vote += 1
        form.save()
        return redirect('New:list')


class VoteView(RedirectView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = self.request.user
        new = get_object_or_404(New, pk=pk)
        print(new.vote)

        if user and new.vote:
            if user.is_authenticated():
                print(new.user)
                if new.vote > 0:
                    new.vote = new.vote + 1
                    new.save()
                    return redirect('New:list')
            return redirect('Profile:sign_up')


@method_decorator(login_required, name='dispatch')
class CommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('New:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.new = New.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(CommentView, self).form_valid(form)
