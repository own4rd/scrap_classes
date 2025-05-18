from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processos.urls')),  # Ajuste para o nome do seu app
]
