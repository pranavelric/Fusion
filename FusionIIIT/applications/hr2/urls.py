from django.conf.urls import url

from . import views

app_name = 'hr2'

urlpatterns = [

    url(r'^$',views.service_book, name='hr2'),
    url(r'^hradmin/$', views.hr_admin, name='hradmin'),
    url(r'^edit/(?P<id>\d+)/$', views.edit_employee_details, name='editEmployeeDetails'),
    url(r'^viewdetails/(?P<id>\d+)/$', views.view_employee_details, name='viewEmployeeDetails'),
    
    # url(r'^servicebook/$', views.serviceBook, name='serviceBook'),

]

