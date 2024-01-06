from django.urls import *
from .views import *
from django.contrib.auth import views as x_auth

urlpatterns = [
      path('login',x_auth.LoginView.as_view(template_name='log.html'),name="login"),
      path('logout',x_auth.LogoutView.as_view(),name="logout"),
      path('add_user/',register_page,name="reg"),
      path('',home,name="menu"),
      path('add_user/create_<str:user_id>_profile',profile_creation,name="make_profile"),
      #path('add_user/create_profile',Profile_creation.as_view(),name="make_profile"),
      
      path('<str:user_id>_profile',the_user_profile,name="show_profile"),
      path('printings',printings,name='prints'),
      path('sport_cars',sport_cars,name='cars'),
      path('websites',web_sites,name='web_sites'),
      path('social_posts',social_media,name='social'),
      path('providers',service_providers,name='providors'),
      path('display_item_num<int:item>:<str:erb>',display_item,name='display_content'),
      path('web_<int:id>',w_item,name='w_item'),
      path('sm_<int:id>',sm_item,name='sm_item'),
      path('post_<int:id>',p_item,name='p_item'),
      path('car_<int:id>',c_item,name='c_item'),
      


]