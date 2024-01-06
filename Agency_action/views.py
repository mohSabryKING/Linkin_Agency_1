from django.http import HttpResponse
from django.shortcuts import *
from .form_model import *
from .models import *
from django.contrib.auth import login
from django.contrib import messages as send
from django.utils.html import *
from django.http import *
from django.views import defaults
from django.utils.translation import gettext as _
from django.views.generic.edit import *


# Create your views here.
def register_page(h):
      print("REGISTER PAGE\n")
      head_title=mark_safe("<h1 class='title'>REGISTER PAGE</h1>")
      user_form=FormUser()
      if h.method=='POST':
            print("post action active")
            user_form=FormUser(h.POST)
            if user_form.is_valid():
                  send.info(h,"form is valid",extra_tags='INFO')
                  loged=user_form.save()
                  print("user name or password is valid and saved")
                  #login(loged,h)
                  print("\n"+str(loged)+"\n")
                  #send.success(h,"username of "+str(loged)+" and its password are valid and saved",extra_tags='SUCCESS')
                  #user_profile=User_profile.objects.create(related_to_user=loged)
                  send.success(h,"username of "+str(loged)+" and its password are valid and saved",extra_tags='SUCCESS')
                  return redirect("make_profile",loged)

            else: 
                  send.error(h,"user name or password is not valid ",extra_tags='ERROR')
                  print("user name or password is not valid")
      
      
      else:
            print("no post action")
      context={'form':user_form,'the_title':head_title,}
      return render(h,'sign_up.html',context)

def profile_creation(h,user_id):
      the_user=User.objects.get(username=user_id)
      #form_model=Profile_creation_Model()
      #login(request,user)
      if h.method=="POST":

            v2=h.POST['in_1']
            v3=h.POST['in_2']
            v4=h.POST['in_3']
            v5=h.POST['in_4']
            profile=User_profile(related_to_user=the_user,client_img=v2,client_name=v3,contracted_with=v4,phone_number=v5)
            return redirect('show_profile',profile)
      else:
       #form_model=Profile_creation_Model()
       send.error(h,"No post acction applied",extra_tags='Error')
      
      return render(h,'create_profile.html',{'user':the_user,'providers':Service_provider.objects.all(),
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()})

class Profile_creation(FormView):
      template_name='create_profile.html'
      success_url='Done_profile'
      form_class=Profile_creation_Form
      def form_valid(self, form):
            return super().form_valid(form)
      

def the_user_profile(h,user_id):

      return render(h,'user_profile.html',{'providers':Service_provider.objects.all(),
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()})



def display_user_profile(h,user_id):
      return HttpResponse(h,"<h1 class='titile'>client "+str(user_id)+" page profile displayed</h1>")


'''
{'head_title_home':head_title,
               'prints':[Printing.objects.create(pk=i) for i in range(30)]
               ,'car_models':[Sport_car.objects.create(pk=i) for i in range(30)]
               ,'social_posts':[Social_media.objects.create(pk=i) for i in range(60)],
                'providers':[Service_provider.objects.create(pk=i) for i in range(7)]
                ,'websites':[Web_site.objects.create(pk=i) for i in range(10)]}

                
                {'head_title_home':head_title,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
'''



def home(h):
      print("menu page")
      
      head_title=mark_safe(f"<h1 class='titile'>"+_("Menu page")+"</h1>")
      print("creating 20 item of printing")
      print("creating 40 item of Sport cars")
      print("creating 60 item of Social media posts")
      print("creating 10 sorts of websites")
      print("creating 5 items of services")
      context={
               'head_title_home':head_title,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()
               
               ,'car_models_c':Sport_car.objects.count()
               ,'social_posts_c':Social_media.objects.count(),
                'providers_c':Service_provider.objects.count()
                ,'websites_c':Web_site.objects.count()
                
                ,'prints_c':Printing.objects.count()
                
                }

                
      return render(h,'menu.html',context)

def display_item(h,item,erb):
      itemx=Web_site.objects.get(pk=item)
      return HttpResponse(f"<h1 style='color:#000' class='title' >{str(itemx)}-{erb}</h1>")



def printings(h):
      print("printings page")
      head_title=mark_safe(_("Printings"))
      context={'head_title_print':head_title,'prints':Printing.objects.all()
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
               
      return render(h,'prints.html',context)

def social_media(h):
      print("social links")
      head_title=mark_safe(_("Social media"))
      context={'head_title_print':head_title,'social_posts':Social_media.objects.all(),
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'social_links.html',context)

def web_sites(h):
      print("websites page")
      head_title=mark_safe(_("All websites"))
      context={'head_title_websites':head_title,'websites':Web_site.objects.all()
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'websites.html',context)

def service_providers(h):
      print("service providers page")
      head_title=mark_safe(_("Service Providers"))
      context={'head_title_print':head_title,'providers':Service_provider.objects.all()
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'providors.html',context)

def sport_cars(h):
      print("sports car page")
      head_title=mark_safe(_("Sport cars"))
      context={'head_title_cars':head_title,'car_models':Sport_car.objects.all()
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'cars.html',context)

def w_item(h,id):
      context={'web':Web_site.objects.get(pk=id)
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'web_item.html',context)

def sm_item(h,id):
      context={'post':Social_media.objects.get(pk=id)
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'post_item.html',context)
def p_item(h,id):
      context={'print':Printing.objects.get(pk=id)
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'print_item.html',context)
def c_item(h,id):
      context={'car':Sport_car.objects.get(pk=id)
               ,
               'prints':Printing.objects.all()
               ,'car_models':Sport_car.objects.all()
               ,'social_posts':Social_media.objects.all(),
                'providers':Service_provider.objects.all()
                ,'websites':Web_site.objects.all()}
      return render(h,'car_item.html',context)





def e400(h,e):
      send.error(h,"Bad request error")
      return defaults.permission_denied(h,e,'ex/e400.html')
def e403(h,e):
      send.error(h,"Auth error")
      return defaults.bad_request(h,e,'ex/e403.html')
def e404(h,e):
      send.error(h,"Page not found")
      return defaults.page_not_found(h,e,'ex/e404.html')
def e500(h):
      send.warning(h,"Server error")
      return defaults.server_error(h,'ex/e500.html')