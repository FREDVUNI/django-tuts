from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    path("delete_item/<int:Todo_id>",views.delete_item,name="delete_item"),

]    