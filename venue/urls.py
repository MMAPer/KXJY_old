from django.urls import path
from . import views

#  在多个app之间，有可能产生同名的url，这时候为了避免反转url的时候产生混淆，可以使用应用命名空间
app_name = 'venue'

#  视图函数反转：reverse('venue:index')

urlpatterns = [
    path('', views.getVenues, name='index'),  # 得到所有数据类别和其包含场馆的信息
    path('label', views.getVenuesLabel),  # 只获得数据类别
    path('label/<labelName>', views.getVenuesByLabel),  # 获取指定数据类别下面包含的场馆
    path('label/delete/<labelName>', views.delLabel),  # 删除指定类别
]