from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("1", views.todo,name="todo"),
    path("2", views.history,name="history"),
    path("3", views.context,name="context"),
    path("4/<int:pk>/",views.edit,name="edit"),
    path("5/<int:id>",views.delete,name='delete')
]