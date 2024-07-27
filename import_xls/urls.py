from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conversor/', include('conversor.urls')),
    path('', lambda request: redirect('upload_file', permanent=True)),  # Redireciona a raiz para o upload
]
