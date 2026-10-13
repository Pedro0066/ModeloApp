from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'products'

router = routers.DefaultRouter()
router.register('', views.ProductViewSet, basename='produtos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('listar/', views.list_products, name='list_products'),
    path('adicionar/', views.add_product, name='add_product'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_product'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)