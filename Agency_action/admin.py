from collections.abc import Mapping
from typing import Any
from django.contrib import admin
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from parler.admin import *
from .models import*
from django import forms
#from .import models
from django.utils.translation import gettext_lazy as _
# Register your models here.

class Login_Admin(admin.AdminSite):
    site_header=_('log_in')
    login_template='Agency_action/admin/login.html'

call_login=Login_Admin(name='admin_model')

class ModelAdmin(admin.AdminSite):
    site_header=_("Linkin Agency")

class Formprints(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(Formprints,self).__init__(*args,**kwargs)
        self.fields['title'].help_text="post your help title model"
    class Meta:
        model = Printing
        fields = '__all__'















class Print_Admin(TranslatableAdmin):
    #form=Formprints
    list_display = ('pk','title','added_in','price_per_item','amount')


class Car_Admin(TranslatableAdmin):
    list_display = ('car_name','added_in')


class Web_site_Admin(TranslatableAdmin):
    list_display = ('web_name','web_type','url_hyperlink','added_in')


class Social_Admin(TranslatableAdmin):
    list_display = ('post_name','added_in','post_img')


class Emp_Admin(TranslatableAdmin):
    list_display = ('emp_name','view_emp_img','salary','added_in')


class Provider_Admin(TranslatableAdmin):list_display = ('service_name','provider')




model_admin_obj=ModelAdmin(name='Admin_page')

model_admin_obj.register(Printing,Print_Admin)



class NameAdmin(TranslatableAdmin):pass

#model_admin_obj.register(User_profile, NameAdmin)





model_admin_obj.register(Web_site,Web_site_Admin)

model_admin_obj.register(Social_media,Social_Admin)

model_admin_obj.register(Sport_car,Car_Admin)
model_admin_obj.register(Emp_model,Emp_Admin)
model_admin_obj.register(Service_provider,Provider_Admin)
model_admin_obj.register(User)



