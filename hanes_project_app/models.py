from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import User
from django.db import models
# from django.forms import models
from django.db.models.signals import post_save

TYPE_CHOICES = (
('A','3 days'),
('1 weeks', '1 weeks'),
('2 weeks', '2 week'),
('1 month', '1 month'),
('2 month', '2 month'),
('3 month', '3 month'),
('4 month', '4 month'),
('5 month', '5 month'),
('6 month', '6 month'),

)
MENU_CHOICES = (
('Arbeit','Arbeit'),
('Gebrauchtes', 'Gebrauchtes'),
('Produkte', 'Produkte'),
)

REGION_CHOICES = (
('Vinschgau','Vinschgau'),
('Burggrafenamt', 'Burggrafenamt'),
('Wipptal', 'Wipptal'),
('Eisacktal', 'Eisacktal'),
('Pustertal', 'Pustertal'),
('Salten-Schlern', 'Salten-Schlern'),
('Bozen', 'Bozen'),
('Uberetsch-Unterland', 'Uberetsch-Unterland'),
)
class Menu_Category(models.Model):
    menu_category = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Add Menu Category"

    def __unicode__(self):
        return u'%s' % (self.menu_category)

class Sub_Category(models.Model):
    menu_category = models.ForeignKey(Menu_Category)
    sub_category = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Add Sub Category"

    def __unicode__(self):
        return u'%s' % (self.sub_category)

class Region(models.Model):
    region = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Add Region"

    def __unicode__(self):
        return u'%s' % (self.region)


class Add_Post_Details(models.Model):
    menu_category = models.CharField(max_length=500, blank=False, null=False,choices=MENU_CHOICES)
    sub_category = models.CharField(max_length=500, blank=False, null=False)
    region = models.CharField(max_length=500, blank=False, null=False,choices=REGION_CHOICES)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    company_name= models.CharField(max_length=100)
    set_timer = models.CharField(max_length=100, choices=TYPE_CHOICES,blank=False, null=False)
    post_time = models.DateField()
    class Meta:
        verbose_name_plural = "Edit Post Details"


class Post_Images(models.Model):
    post = models.ForeignKey(Add_Post_Details)
    post_image = models.ImageField(upload_to='post_images/', blank=True, null=True )

    class Meta:
        verbose_name_plural = "Add Post Images"

    def __unicode__(self):
        return u'%s' % (self.post)

class AdvertisementDetails(models.Model):
    ads_category = models.CharField(max_length=100)
    Ads_images = models.ImageField(upload_to='Advertise Images/',max_length=1000,blank=False, null=False)
    class Meta:
        verbose_name_plural = "Add New Advertise"

    def __unicode__(self):
        return u'%d' % (self.id)