"""
URL configuration for TerceraPreentregaForastieri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App3raEntrega.views import ingresar_paciente, ingresar_consumible, trabajo_realizado, mostrar_paciente, show_html


urlpatterns = [
    path('ingresar_paciente/', ingresar_paciente),
    path('ingresar_consumible/', ingresar_consumible),
    path('trabajo/', trabajo_realizado),
    path('show/', show_html),
    path('pacientes/', mostrar_paciente),
]
