
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('login/',views.login),
    path("showCakes/<id>",views.showCakes),
    path('viewDetails/<id>',views.viewDetails),
    path('signup',views.signUp),
    path('signout',views.signOut),
    path('addtocart',views.addTocart),
    path('showAllCartItems',views.showAllCartItems)
]