from django.shortcuts import render, get_object_or_404
from .models import Items
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'item': Items.objects.all()
    }
    return render(request, 'homepage/home.html', context)


class ItemListView(ListView):
    model = Items
    template_name = 'homepage/home.html'  # app/model_viewtype.html
    context_object_name = 'item'
    ordering = ['-date_posted']
    paginate_by = 6


# views for posts from  an individual user
class UserItemListView(ListView):
    model = Items
    template_name = 'homepage/user_item.html'  # app/model_viewtype.html
    context_object_name = 'item'
    paginate_by = 6

    def get_queryset(self): # filtering based on username
        user = get_object_or_404( User, username=self.kwargs.get('username') )
        return Items.objects.filter(author=user).order_by('-date_posted')

class ItemDetailView(DetailView):
    model = Items


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Items
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Items
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Items
    success_url = '/'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False


def aboutus(request):
    return render(request, 'homepage/about.html', {'title': 'About'})
