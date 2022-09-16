from . import views
from django.urls import path
urlpatterns = [

    path('home', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),

]
