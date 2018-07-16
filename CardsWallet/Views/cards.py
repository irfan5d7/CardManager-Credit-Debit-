from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from CardsWallet.models import Cards
from CardsWallet.forms import *


def show_cards(request):
    context_dict = {}
    context_dict['result_list'] = None
    try:
        cards = Cards.objects.filter(user = request.user)
        context_dict['cards'] = cards
    except:
        pass
    return render(request,'cards.html',context_dict)











class CreateCardView(CreateView):
    # login_url = '/login/'
    model = Cards
    template_name = 'add_card.html'
    def get_context_data(self, **kwargs):
        context = super(CreateCardView, self).get_context_data(**kwargs)
        # profile = UserProfile.objects.filter(user__username=self.request.user.username)
        # context['prof'] = profile
        return context
    def post(self, request, *args, **kwargs):
        card_form = AddCard(request.POST,request.FILES)
        if card_form.is_valid():
            card = card_form.save(commit = False)
            card.user = self.request.user
            card.save()
        return redirect('CardsWallet:index')

class UpdateCardView(UpdateView):
    # login_url = '/login/'
    model = Cards
    form_class = AddCard
    template_name = 'add_card.html'

    def get_success_url(self):
        return reverse('CardsWallet:index')

    def get_context_data(self, **kwargs):
        context = super(UpdateCardView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        card = Cards.objects.get(id=kwargs.get('pk'))
        form = AddCard(request.POST, instance=card)
        form.save()
        return redirect('CardsWallet:index')


class DeleteProductView(DeleteView):
    # login_url = '/login/'
    model = Cards
    success_url = reverse_lazy('CardsWallet:index')
    def get_success_url(self):
        return reverse('CardsWallet:index')
    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)
    def post(self, request, *args, **kwargs):
        self.delete(request,args,kwargs)
        return redirect('CardsWallet:index')

