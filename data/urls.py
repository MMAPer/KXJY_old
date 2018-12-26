from django.urls import path
from . import views

#  在多个app之间，有可能产生同名的url，这时候为了避免反转url的时候产生混淆，可以使用应用命名空间
app_name = 'data'

#  视图函数反转：reverse('venue:index')
#  数据层级：label->venue->item
urlpatterns = [
    path('', views.getDatas, name='index'),
    path('<labelName>/', views.getDataByLabel),
    path('<labelName>/<venueName>/', views.getDataByLabelAndName),
    path('search/<venueName>/<itemName>/', views.searchData),
    path('detail/html/<labelName>/<venueName>/<itemName>', views.getDetailHtml),
    path('detail/<labelName>/<venueName>/<itemName>', views.getDetailData),
    path('delete/<labelName>/<venueName>/<itemName>', views.deleteData),
    path('update/html/<labelName>/<venueName>/<itemName>', views.getUpdateDataHtml),
    path('update/<labelName>/<venueName>/<itemName>', views.updateData),
    path('add/html/get/', views.getAddDataHtml),
    path('add/', views.addData),

]