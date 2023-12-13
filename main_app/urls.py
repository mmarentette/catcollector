from django.urls import path 

# Imports all of the functions in the views.py file and attaches them as eys on the views object here
# The . means current directory
from . import views

# Don't forget the trailing slashes in the path strings! (except for home path)
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    # <int:cat_id> is how django does params, and it will automatically detect numbers
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # CBV (class-based view) must be rendered using the as_view() method
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    # Notice that we put 'cats/create' after 'cats/<int:cat_id>/' - we couldn't do this in Express, but we can in Django because for the previous url, it's looking for an integer specifically, so create wouldn't match
    # CBVs expect pk to be the param name by convention
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'), # At first, I accidentally included parens - add_feeding() - here, but we don't do that here! We don't want to call the function until the path is matched (I think)
]
