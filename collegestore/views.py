from django.shortcuts import render
from .forms import MembershipForm
from .models import Membership
from django.views import View


class HomeView(View):
 def get(self, request):
  form = MembershipForm()
  candidates = Membership.objects.all()
  return render(request, 'myapp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = MembershipForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'myapp/home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = MembershipForm.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})