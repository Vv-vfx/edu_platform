from django.urls import path, include
from .router import router
from .views import UpdateTokenView

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('update_token/', UpdateTokenView.as_view(), name='update_token'),
    ]