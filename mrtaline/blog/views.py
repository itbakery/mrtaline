# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView, UpdateView
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from models import Entry
# Create your views here.


class BlogListing(ListView):
    queryset = Entry.objects.published()
    model = Entry
    paginate_by = 2


# myapp/entry_form.html

class BlogCreate(CreateView):
    model = Entry
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BlogCreate, self).dispatch(*args, **kwargs)


class BlogDetail(DetailView):
    model = Entry


class BlogUpdate(UpdateView):
    model = Entry

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.object.pk})

class BlogDelete(DeleteView):
    model = Entry
    success_url = '/blog/'
