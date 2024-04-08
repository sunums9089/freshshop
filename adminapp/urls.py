from django.urls import path
from.import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('form',views.form,name='form'),
    path('table',views.table,name='table'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('usertable',views.usertable,name='usertable'),
    path('reg_table',views.reg_table,name='reg_table'),
    path('check_table',views.check_table,name='check_table'),
    path('adminhome',views.adminhome,name='adminhome')
]