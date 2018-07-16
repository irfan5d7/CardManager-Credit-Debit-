from django.conf.urls import url
from django.urls import path

from CardsWallet.Views import *
from CardsWallet.Views.login import SignUpController, LoginController, logout_user

app_name = 'CardsWallet'
urlpatterns =[
    url('cards/',show_cards,name='cards_views'),
    url(r'^signup/$',SignUpController.as_view(),name = 'signup'),
    path('login/',LoginController.as_view(),name='login'),
    path('logout/',logout_user,name = 'logout'),
    # url('add_cards/',CreateCardView,name='add_card'),

    ]