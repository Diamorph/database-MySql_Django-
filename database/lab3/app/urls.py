from django.conf.urls import url
from . import views
from .views import PharmacyView, MedicView, PillsView


urlpatterns = [
    url(r'^add-pharmacy/$', PharmacyView.as_view() , name = 'add-pharmacy'),
    url(r'^add-medic/$', MedicView.as_view() , name = 'add-medic'),
    url(r'add-pills/$',PillsView.as_view(), name='add-pills'),
    url(r'del/ph/(\d+)/$', views.del_pharmacy),
    url(r'del/md/(\d+)/$', views.del_medic),
    url(r'del/pill/(\d+)/$', views.del_pill),
    url(r'edit/ph/(\d+)/$', views.edit_pharmacy),
    url(r'edit/md/(\d+)/$', views.edit_medic),
    url(r'edit/pill/(\d+)/$', views.edit_pill),
    url(r'^$', views.main),
]