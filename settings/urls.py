from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('userapp.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include('api.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),

]
