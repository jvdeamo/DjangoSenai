"""
URL configuration for projetoDjango project.

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
from django.contrib import admin
from appDjango import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('loja/', views.indexLoja, name='indexLoja'),
    path('loja/estoque', views.estoqueLoja, name='estoqueLoja'),
    path('loja/adicionar', views.adicionarEstoque, name='adicionarEstoque'),
    path('loja/info/<int:id>', views.infoEstoque, name='infoEstoque'),
    path('loja/editar/<int:id>', views.editarEstoque, name='editarEstoque'),
    path('loja/excluir/<int:id>', views.excluirProduto, name='excluirProduto'),
]
