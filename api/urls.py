from django.urls import path
from .views import indexView 
urlpatterns = [
    path('',indexView,name='index_view'),
    # path('',loginView,name='login_view')
]
