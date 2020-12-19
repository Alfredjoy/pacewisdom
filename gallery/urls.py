from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.home,name='home'),
    path('category/<id>',views.category,name='category'),
    path('new_category',views.new_category,name='new_category'),
]