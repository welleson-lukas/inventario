from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import cadastrar_equipamento

app_name = 'equipamento'

urlpatterns = [
    path('', views.ListaEquipamento.as_view(), name='index'),
    path('desktop/', views.ComputadoresView.as_view(), name='desktop'),
    path('laptop/', views.LaptopView.as_view(), name='laptop'),
    path('monitor/', views.MonitorView.as_view(), name='monitor'),
    path('nobreak/', views.NobreakView.as_view(), name='nobreak'),
    path('roteador/', views.RoteadorView.as_view(), name='roteador'),
    path('switch/', views.SwitchView.as_view(), name='switch'),
    path('smartphone/', views.SmartphoneView.as_view(), name='smartphone'),
    path('inativos/', views.InativosView.as_view(), name='inativos'),
    path('cadastrar/', cadastrar_equipamento, name='cadastrar'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)