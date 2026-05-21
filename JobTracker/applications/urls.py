from django.urls import path
from . import views

urlpatterns=[
    path("",view=views.application_list,name='application-list'),
    path("summary/",view=views.application_summary),
    path("<int:key>/generate-followup/",view=views.generate_followup),
    path("<int:key>/",view=views.application_detail,name='application-detail'),
]