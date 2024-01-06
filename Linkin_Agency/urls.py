"""
URL configuration for Linkin_Agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import *
from django.conf.urls.static import *
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import *
from django.conf import settings
from Linkin_Agency.settings import*
from Agency_action.admin import *
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import views as x_auth

urlpatterns = i18n_patterns(
    path('linkin_admin/', model_admin_obj.urls),
    path('', include('Agency_action.h')),
    path('rosetta/', include('rosetta.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
'''
urlpatterns+=path('logout',x_auth.LogoutView.as_view(),name='logout')
urlpatterns+=path('login',x_auth.LoginView.as_view(template_name='log.html'),name='login')'''
admin.site.index_title='view data'
admin.site.site_header=_('Linkin_agency')
admin.site.site_title=_('Linkin_agency')
handler400="Agency_action.views.e400"
handler403="Agency_action.views.e403"
handler404="Agency_action.views.e404"
handler500="Agency_action.views.e500"