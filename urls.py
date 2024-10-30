"""
URL configuration for itsofolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# itsofolio/urls.py
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from .views import homepage  # type: ignore # Make sure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),  # Ensure portfolio is included
    path('', homepage, name='homepage'),             # Root URL now leads to homepage
]

