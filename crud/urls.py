from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #CREATE
    path('create/',views.Create.as_view(),name="create"),
    #READ
    path('',views.Read.as_view(),name="read"),
    #UPDATE
    path('update/<int:pk>/',views.Update.as_view(),name="update"),
    #DELETE
    path('delete/<int:pk>/',views.Delete.as_view(),name="delete"),

]
