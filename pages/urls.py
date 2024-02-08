from django.urls import path
from . import views

urlpatterns = [ 
    # path('', views.index_pages, name='index_pages'), 
    path('<str:pagename>', views.index_pages, name='index_pages'), 
    path('', views.index_pages, {'pagename': ''}, name='index_pages'), 
] 

