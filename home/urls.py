# home URLS

from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Add_expense',views.add_expense,name='Add_expense'),
    path('<int:id>/',views.delete_expense,name='delete_expense'),
    path('update_expense/<int:id>',views.update_Expense,name='update_expense'),
]

