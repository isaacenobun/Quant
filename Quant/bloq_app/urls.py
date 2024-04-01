from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('block-params/', views.params1, name='block-params'),
    path('door-params/', views.params2, name='door-params'),
    path('window-params/', views.params3, name='window-params'),
    path('openings/', views.params4, name='opening-params'),
    path('details/', views.details, name='details'),
    # Special
    path('cancel/', views.cancel, name='cancel'),
    path('add-block-type/', views.add_block_type, name='add-block-type'),
    path('delete-block-type/<int:blockId>', views.delete_block_type, name='delete-block-type'),
    path('add-door-type/', views.add_door_type, name='add-door-type'),
    path('delete-door-type/<int:doorId>', views.delete_door_type, name='delete-door-type'),
    path('add-window-type/', views.add_window_type, name='add-window-type'),
    path('delete-window-type/<int:windowId>', views.delete_window_type, name='delete-window-type'),
    path('add-opening-type/', views.add_opening_type, name='add-opening-type'),
    path('delete-opening-type/<int:openingId>', views.delete_opening_type, name='delete-opening-type'),
    # Edits
    path('block-params-edit/', views.params1_edit, name='block-params-edit'),
    path('add-block-type-edit/', views.add_block_type_edit, name='add-block-type-edit'),
    path('delete-block-type-edit/<int:blockId>', views.delete_block_type_edit, name='delete-block-type-edit'),
    path('door-params-edit/', views.params2_edit, name='door-params-edit'),
    path('add-door-type-edit/', views.add_door_type_edit, name='add-door-type-edit'),
    path('delete-door-type-edit/<int:doorId>', views.delete_door_type_edit, name='delete-door-type-edit'),
    path('window-params-edit/', views.params3_edit, name='window-params-edit'),
    path('add-window-type-edit/', views.add_window_type_edit, name='add-window-type-edit'),
    path('delete-window-type-edit/<int:windowId>', views.delete_window_type_edit, name='delete-window-type-edit'),
    path('openings-edit/', views.params4_edit, name='opening-params-edit'),
    path('add-opening-type-edit/', views.add_opening_type_edit, name='add-opening-type-edit'),
    path('delete-opening-type-edit/<int:openingId>', views.delete_opening_type_edit, name='delete-opening-type-edit'),
    # Report
    path('report/', views.report, name='report'),
]