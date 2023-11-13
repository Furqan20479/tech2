

from django.urls import path
from . import views
urlpatterns = [


    path("", views.frount_page, name='base.html'),
    path("signup/", views.signup_user, name="signup.html"),
    path('placeorder/', views.placeorder, name="mtemp.html"),
    path("login/", views.login_view, name="login.html"),
    path('logout/', views.logout_user, name='logout'),
    path('users/', views.users.as_view()),
    path('items/', views.items.as_view())

]



  
