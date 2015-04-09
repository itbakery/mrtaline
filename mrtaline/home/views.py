# from django.shortcuts import render
# import json
from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from braces import views
from reports.models import Portal, Place
from notes.models import Message, Msgtype
from announces.models import Announce
from activities.models import Activity
from businesses.models import Business
from forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.gis.geos import fromstr
# Create your views here.


class IndexView(ListView):
    #model = Message
    queryset = Message.objects.published()
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['Msgtypes'] = Msgtype.objects.all()
        ctx['Announces'] = Announce.objects.published()
        ctx['Activities'] = Activity.objects.published()
        ctx['Businesses'] = Business.objects.all()
        return ctx


class ThemesView(TemplateView):
    template_name = "home/themes.html"


class AboutView(TemplateView):
    template_name = "home/about.html"


class MapView(TemplateView):
    template_name = "home/map.html"


class SuccessView(TemplateView):
    template_name = "home/success.html"


class SignUpView(views.AnonymousRequiredMixin,
                 views.FormValidMessageMixin,
                 CreateView):
    form_class = RegistrationForm
    form_valid_message = "Thank you for signup"
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        resp = super(SignUpView, self).form_valid(form)
        Portal.objects.create(user=self.object, title=self.object.username)
        return resp


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(views.LoginRequiredMixin, views.MessageMixin, RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.messages.success("You've been logged out. Come back soon!")
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)


def save_issue(request):
    if request.method == 'POST' and request.is_ajax:
        response_data = {}
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        lat = request.POST.get('lat', None)
        lng = request.POST.get('lng', None)
        token = request.POST.get('csrf', None)
        token = request.POST.get('csrf', None)
        user = request.POST.get('user', None)
        reporttype = request.POST.get('reporttype', None)

        response_data['title'] = title
        response_data['description'] = description
        response_data['lat'] = lat
        response_data['lng'] = lng
        response_data['token'] = token
        # current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
        # split string with with delimeters
        # str.split(', ')
        point = fromstr("POINT(%s %s)" % (lng, lat))
        print response_data
        # print p
        # print point
        # p = Portal.objects.get(title=user)
        # u = User.objects.get(username=user)
        # print p
        # p = Portal.objects.get(title=user)
        u = User.objects.get(username=user)
        point_obj = Place(title=title, description=description, geom=point, user=u, reporttype=reporttype)
        # print point_obj
        point_obj.save()
        # print point_obj.created
        response_data['created'] = point_obj.created
        # request.POST
        # {"latlng": "13.733382,100.521061", "csrfmiddlewaretoken": "F11cng7GGhHqmAsnHhrCQAIg5nVOijMT", "name": "aaaaa", "report_type": "asset", "address": "aaaaaa"}
        # return render(request,json.dumps(request.POST),content_type='application/json')
        # django 1.7 use JsonResponse
        # return  render(request,'home/index.html',JsonResponse(response_data))
        return HttpResponse(JsonResponse(response_data), content_type="application/json")
    else:
        msg = {"nothing to see": "this isn't happening"}
        return HttpResponse(JsonResponse(msg), content_type="application/json")


def remove_issue(request):
    if request.method == 'POST' and request.is_ajax:
        latlng = request.POST.get('latlng', None)
        p = latlng.split(',')
        point = fromstr("POINT(%s %s)" % (p[1], p[0]))
        Place.objects.get(location=point).delete()
        response_data = {"progress": "it works!"}
        return HttpResponse(JsonResponse(response_data), content_type="application/json")
    else:
        msg = {"progress": "it fails"}
        return HttpResponse(JsonResponse(msg), content_type="application/json")


