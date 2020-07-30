from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from App.forms import UserForm
from App.models import User
# Create your views here.
class BaseView(TemplateView):

template_name = 'App/base.html'

class NextView(CreateView):

    model = User

    fields = '__all__'
    context_object_name = 'form'

    template_name = 'App/user_form.html'
