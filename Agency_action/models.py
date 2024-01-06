from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.conf import settings

# Create your models here.
#URL default:https://www.facebook.com/groups/604256213502156/?hoisted_section_header_type=recently_seen&multi_permalinks=1432232637371172
default_url="https://www.facebook.com/groups/604256213502156/?hoisted_section_header_type=recently_seen&multi_permalinks=1432232637371172"
default_info="Lorem ipsum dolor sit amet consectetur adipisicing elit. Est consequuntur earum cupiditate nobis provident, amet voluptate molestias corrupti! Veniam."



class Emp_model(TranslatableModel):
    trans_x=TranslatedFields(
    emp_name=models.CharField(verbose_name=_("emp_name"),max_length=40,default="Ahmed hany"),
    emp_img=models.ImageField(verbose_name=_("emp_img"),upload_to="emps of %d %M %Y",default="user.png"),
    salary=models.PositiveIntegerField(verbose_name=_("salary"),default=3000),
    position=models.CharField(verbose_name=_("position"),max_length=20,default="Sales"),)
    
    added_in=models.DateTimeField(auto_now_add=True)
    class Meta:
       verbose_name=_("emp_profile") 
       verbose_name_plural=_("emps_profile")
    
    
    def view_emp_img(self):
        return mark_safe(f"<img width='64px' height='64px' src={self.emp_img.url}/>")
        

    def __str__(self):return str(self.added_in)
    
    def print_model(self):
        return mark_safe(f"<div><h1 class='title'>{self.emp_name}:{self.position}</h1><img class='img_model2' src={self.emp_img.url}/><br><span>{self.added_in}</span></div>")


class User_profile(TranslatableModel):
    '''
    client_img
    client_name
    contracted_with
    phone_number
    '''
    related_to_user = models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name=_("related_to_user"),related_name="used_by", on_delete=models.SET_NULL,null=True),
    
    trans_x=TranslatedFields(
    client_img = models.ImageField(verbose_name=_("client_img"),upload_to="client face of %d %M %Y",default="user.png"),
    client_name = models.CharField(verbose_name=_("client_name"),max_length=50,default="Amir client"),
    #contracted_with = models.ForeignKey(Emp_model, related_name='contracted_by', on_delete=models.CASCADE),
    phone_number=models.PositiveIntegerField(verbose_name=_("phone_number"),default=1094128969),
    )
    class Meta:
       verbose_name=_("user_profile") 
       verbose_name_plural=_("user_profile")
       ordering=['pk']
    added_in=models.DateTimeField(auto_now_add=True)
    def __str__(self):return str(self.added_in)
    def phone_number_call(self):return "0"+str(self.phone_number)
    def print_model(self):return mark_safe(f"NONE User")



class Social_media(TranslatableModel):
    Platform=[('Facebook','Facebook'),('Insta','Insta'),('Whatsapp','Whatsapp'),]
    post_for_client=models.ForeignKey(User_profile,related_name=_("add_to_x"),on_delete=models.SET_NULL,null=True),
   
    trans_x=TranslatedFields(
    post_name=models.CharField(verbose_name=_("post_name"),max_length=40,default="Post title"),
    platform_type = models.CharField(verbose_name=_("platform_type"),max_length = 350,choices=Platform,default=Platform[0]),
    url_hyperlink=models.URLField(verbose_name=_("url_hyperlink"),max_length=350,default=default_url),
    postgraph = models.ImageField(verbose_name=_("postgraph"),upload_to="postgraphs_",default="soc.jpg"),
    bio = models.TextField(verbose_name=_("bio"),max_length=400,default=default_info),
    campagin_cost=models.PositiveIntegerField(verbose_name=_("campagin_cost"),default=3000),)
    
    
    added_in=models.DateTimeField(auto_now_add=True)
    
    class Meta:
       verbose_name=_("social_media") 
       verbose_name_plural=_("social_media")
    def post_img(self):return mark_safe(f"<img class='' src={self.postgraph.url}/>")
    
    def __str__(self):return str(self.added_in)
    def print_model(self):
        return mark_safe(f"<div><h1 class='title'>{self.post_name}:{self.campagin_cost} EGP</h1><img class='img_model3' src={self.postgraph.url}/><br><span>{self.added_in}</span></div>")



class Printing(TranslatableModel):
    Type=[('Laser','Laser'),('Paper','Paper'),('Baner','Baner'),(' Stuff','Stuff'),]
    for_client=models.ForeignKey(User_profile,related_name=_("for_client_x1"),on_delete=models.SET_NULL,null=True),
    
    trans_x=TranslatedFields(
    campagin_cost = models.PositiveBigIntegerField(verbose_name=_("campagin_cost"),default=2000),
     print_type = models.CharField(verbose_name=_("print_type"),max_length = 50,choices=Type,default=Type[0]),
    
     title=models.CharField(verbose_name=_("title"),max_length=40,default="Printing title"),
     printing_model = models.ImageField(verbose_name=_("printing_model"),upload_to="printings of %d %M %Y",default="prints.jpg"),
     bio = models.TextField(verbose_name=_("bio"), max_length=400,default=default_info),
     price_per_item=models.FloatField(verbose_name=_("price_per_item"),default=1.50,max_length=300.00),
     amount=models.PositiveSmallIntegerField(verbose_name=_("amount"),default=20),
     
     )
    
    
    added_in=models.DateTimeField(auto_now_add=True)
    class Meta:
       verbose_name=_("prints") 
       verbose_name_plural=_("prints")
       ordering = ["pk"]
    def genral_amount_cost(self):
        return str(self.price_per_item*self.amount)+" EGP"
    def __str__(self):return str(self.title)
    def print_model(self):
        return mark_safe(f"<div><h1 class='title'>{self.title}:{self.amount}</h1><img class='img_model3' src={self.printing_model.url}/><br><span>{self.added_in}</span></div>")



class Web_site(TranslatableModel):
    Web_Type=[('Static','Static'),('Dynamic','Dynamic'),]
    for_client=models.ForeignKey(User_profile,related_name=_("for_client_x2"),on_delete=models.SET_NULL,null=True),
   
    trans_x=TranslatedFields(
    web_name=models.CharField(verbose_name=_("web_name"),max_length=20,default="web site x"),
    web_type = models.CharField(verbose_name=_("web_type"),max_length = 50,choices=Web_Type,default=Web_Type[0]),
    logo=models.ImageField(verbose_name=_("logo"),upload_to="website of %d %M %Y",default="web2.jpg"),
    url_hyperlink=models.URLField(verbose_name=_("url_hyperlink"),max_length=90,default="https://www.w3schools.com/"),
     bio = models.TextField(verbose_name=_("bio"), max_length=400,default=default_info),
    )
    added_in=models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering=['pk']
       verbose_name=_("web_sites") 
       verbose_name_plural=_("web_sites")
    def __str__(self):return str(self.added_in)

    def print_model(self):
        return mark_safe(f"<div><h1 class='title'>{self.web_name}:{self.web_type}</h1><img class='img_model3sm' src={self.logo.url}/><br><span>{self.added_in}</span></div>")
    def print_model_1(self):
        return mark_safe(f"<div><h1 class='title'>{self.web_name}</h1></div>")
    

class Sport_car(TranslatableModel):
    for_client=models.ForeignKey(User_profile,related_name=_("for_client_x3"),on_delete=models.SET_NULL,null=True),
    
    trans_x=TranslatedFields(
    car_name=models.CharField(verbose_name=_("car_name"),max_length=35,default="Dodge challenger 2006"),
    car_poster=models.ImageField(verbose_name=_("car_poster"),upload_to="car photo of %d %MM %YYYY",default="car.jpg"),
    
    bio = models.TextField(verbose_name=_("bio"), max_length=400,default=default_info),
    )
    added_in=models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering=['pk']
       verbose_name=_("cars")
       verbose_name_plural=_("cars")
    def __str__(self):return str(self.for_client)
    
    def print_model(self):
        return mark_safe(f"<div><h1 class='title'>{self.car_name}</h1><img class='img_model3sm' src={self.car_poster.url}/><p>{self.bio}</p><span>{self.added_in}</span></div>")
    
    def print_model_2(self):
        return mark_safe(f"<div><h1 class='title'>{self.car_name}</h1><span>{self.added_in}</span></div>")
    

    def print_model_1(self):
        return mark_safe(f"<div style='background-image:url({self.car_poster.url});background-size:cover;margin:10px;'><div style='margin:10px;;background-color:#00000080;border-raduis:10px;'><h1 class='title'>{self.car_name}</h1><span>{self.added_in}</span></div></div>")


class Service_provider(TranslatableModel):
    for_client=models.ForeignKey(User_profile,related_name=_("for_client_x4"),on_delete=models.SET_NULL,null=True),
    
    trans_x=TranslatedFields(
    service_name=models.CharField(verbose_name=_("service_name"),max_length=35,default="Dodge challenger 2006"),
    service_info = models.TextField(verbose_name=_("service_info"),max_length=400,default=default_info),
    provider=models.ForeignKey(Emp_model,related_name="provided_by",on_delete=models.CASCADE,null=True,blank=True),
    )
    
    added_in=models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering=['pk']
       verbose_name=_("providers")
       verbose_name_plural=_("providers")
    
    
    

    def __str__(self):return str(self.for_client)
    
    def print_model(self):
        return mark_safe(f"<div><h1 class='title'>{self.provider}:{self.service_name}</h1><p>{self.service_info}</p><span>{self.added_in}</span></div>")


    
