from django import forms
from Home.models import Candidate

class AddCandidateForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    class Meta:
        model = Candidate
        fields = ['id','name','vote_count']