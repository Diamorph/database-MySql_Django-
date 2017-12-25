from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^write-ph/$', views.write_pharmacy),
    url(r'^write-med/$', views.write_medic),
    url(r'^add-pills/$', views.add_pills),
    url(r'^del/(\d+)/$', views.delete),
    url(r'^edit/(\d+)/$', views.edit),
    url(r'^$', views.index),
    url(r'^search-ph/$', views.search_ph),
    url(r'^search-med/$', views.search_med),
    url(r'^search-bool/$',views.search_boolean),
]