from django.urls import path

from Home.views import CandidateView, DeleteCandidateView, PollView, UpdateCandidateView

urlpatterns = [
    path('',PollView.as_view(), name='polls'),
    path('candidate-lists/',CandidateView.as_view(), name='candidate_lists'),
    path('update-candidate/<int:id>',UpdateCandidateView.as_view(), name='update-candidate'),
    path('delete-candidate/<int:id>',DeleteCandidateView.as_view(), name='delete-candidate'),
    
    # path('login/',LoginView.as_view(), name='login')
]
