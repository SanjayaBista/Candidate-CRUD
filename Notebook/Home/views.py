from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.views.generic import View
from Home.models import Candidate
from Home.forms import AddCandidateForm
from django.contrib.auth import authenticate, login

class PollView(CreateView):
    model = Candidate
    form_class = AddCandidateForm
    template_name = 'polls.html'
    success_url = '/'

class CandidateView(TemplateView):
    template_name = "candidate_lists.html"
    def get_context_data(self, **kwargs):
        return {
            'candidate': Candidate.objects.all(), 
        }
        
class UpdateCandidateView(UpdateView):
    model = Candidate
    form_class = AddCandidateForm
    pk_url_kwarg = 'id'
    template_name = 'polls.html'
    success_url = '/'

class DeleteCandidateView(DeleteView):
    model = Candidate
    pk_url_kwarg = 'id'
    template_name = 'polls.html'
    success_url = '/'
    
# class LoginView(View):
    
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/form')
#             else:
#                 return HttpResponse("User Not Found")
#         else:
#             return HttpResponseRedirect(settings.LOGIN_URL)
