from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from graphene_django.views import GraphQLView

urlpatterns = [
    path('django/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', include('Inventario.urls')),
    path('admin/', include('django.contrib.auth.urls')),
    path('', include('Prestamo.urls')),
]

urlpatterns += staticfiles_urlpatterns()
