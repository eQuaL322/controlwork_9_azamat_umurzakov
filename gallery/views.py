from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.models import UserProfile
from gallery.forms import PhotoForm
from gallery.models import Photo


# Create your views here.
class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/photo_list.html'
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'gallery/photo_detail.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorited_users'] = UserProfile.objects.filter(favorites=self.object)
        return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/photo_create.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                photo = form.save(commit=False)
                photo.author = request.user
                photo.save()
                return redirect('index')
            else:
                context = {'form': form}
                return self.render_to_response(context)
        else:
            return HttpResponseForbidden()


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/photo_update.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'gallery/photo_delete.html'
    success_url = reverse_lazy('index')
