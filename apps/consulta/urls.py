from django.conf.urls import url,include
from apps.consulta.views import consulta_view
from django.urls import path

urlpatterns = [
    url(r'^$', consulta_view),
]
