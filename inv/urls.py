from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_form, name="login_form"),
    path("login_view", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("item_view", views.item_view, name="item_view"),
    path("add_dev", views.add_dev, name="add_dev"),
    path("add_item", views.add_item, name="add_item"),
    path("add_comp", views.add_comp, name="add_comp"),
    path("add_checkclean", views.add_checkclean, name="add_checkclean"),
    path("check_in", views.check_in, name="check_in"), # not being used
    path("modify", views.modify, name="modify"),
    path("update", views.update, name="update"),
    #path('<int:barcode>', views.barcode, name='barcode'),   
]