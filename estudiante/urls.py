from django.conf.urls import url
from .views import EstudianteCreate, EstudianteList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registro/$', login_required(EstudianteCreate.as_view()), name='estudiante_registro'),
    url(r'^$', login_required(EstudianteList.as_view()), name='estudiante_lista'),
]
