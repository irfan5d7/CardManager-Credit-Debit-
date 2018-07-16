from django.conf.urls import url
from django.urls import path

from CardsWallet.Views import *
from CardsWallet.Views.login import SignUpController

app_name = 'CardsWallet'
urlpatterns =[
    url('cards/',show_cards,name='cards_views'),
    url(r'^signup/$',SignUpController.as_view(),name = 'signup'),

    ]