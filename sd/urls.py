from django.urls import path
from . import views

urlpatterns = [
    path('',views.name,name='name'),
    path('2',views.py, name='py'),
    path('3',views.j,name='j'),
    path('4',views.q,name='q'),
    path('5',views.pro,name='pro'),
    path('one/<int:pk>',views.display,name='display'),
    path('two/<int:ab>',views.edit,name='edit'),
    path('add',views.create,name='create'),
]