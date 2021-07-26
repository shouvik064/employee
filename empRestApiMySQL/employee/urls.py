from django.conf.urls import url 
from employee import views 
 
urlpatterns = [ 
    url(r'^api/employee$', views.employee_list),
    url(r'^api/employee/(?P<pk>[0-9]+)$', views.employee_detail),
    url(r'^api/employee/published$', views.employee_list_published)
]
