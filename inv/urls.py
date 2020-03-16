from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_form, name="login_form"),
    path("login_view", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("item_view", views.item_view, name="item_view"),
    path("check_in", views.check_in, name="check_in"), # not being used
    path("modify", views.modify, name="modify"),
    path('<barcode>', views.barcode, name='barcode'),   
]