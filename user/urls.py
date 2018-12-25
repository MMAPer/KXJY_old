from django.urls import path
from . import views

#  在多个app之间，有可能产生同名的url，这时候为了避免反转url的时候产生混淆，可以使用应用命名空间
app_name = 'user'

#  视图函数反转：reverse('venue:index')

urlpatterns = [
    path('', views.getUsers, name='index'),
    path('add/', views.addUser),
    path('delete/<username>', views.deleteUser),
    path('update/<username>', views.updateUser),
]