from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('block-params/', views.params1, name='block-params'),
    path('door-params/', views.params2, name='door-params'),
    path('window-params/', views.params3, name='window-params'),
    path('openings/', views.params4, name='openings-params'),
    path('details/', views.details, name='details'),
    # Special
    path('cancel/', views.cancel, name='cancel'),
    path('add-block-type/', views.add_block_type, name='add-block-type'),
    
]