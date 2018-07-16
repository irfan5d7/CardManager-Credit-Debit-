from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import *

class CreateCardView(CreateView):
    login_url = '/login/'