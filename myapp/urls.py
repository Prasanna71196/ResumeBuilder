from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('templates',views.templates,name='templates'),
    path('details',views.details,name='details'),
        path('template1',views.template1,name='template1'),
            path('template2',views.template2,name='template2'),
                path('template3',views.template3,name='template3'),
    path('resume',views.resume,name='resume')
]