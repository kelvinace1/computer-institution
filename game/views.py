from django.contrib.messages.views import SuccessMessageMixin
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Course
from game import models
from .forms import ContactForm

# Create your views here.
def about(request):
    return render(request, 'game/about.html')

class Home(ListView):
    model = Course
    template_name = 'game/home.html'
    context_object_name = 'courses'
    #ordering = ['-date']

class Detail(DetailView, SuccessMessageMixin):
    model = Course
    template_name = 'game/course_detail.html'
    #success_message = 'your post has been created'
  

class Create(SuccessMessageMixin, CreateView,):
    model = Course
    fields = ['general_computing', 'operating_system', 'ms_excel',
              'word_processing', 'presentation', 'corel_draw',
               'adobe_photoshop','data_processing', 'networking', 
               'information_technology', 'total']
    success_message = 'grades has been added'
    
    
    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
        
def topics(request):
    return render(request, 'game/topics.html')

class Contact(FormView):
    form_class = ContactForm
    template_name = 'game/contact.html'
    success_url = '/'
    print(form_class)
    