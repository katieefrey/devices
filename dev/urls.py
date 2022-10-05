from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('borrowingpolicy',views.borrowingpolicy, name="borrowingpolicy"),
    path('type/<typepage>', views.typepage, name='typepage'),
    path('<devname>', views.devname, name='devname'),
]