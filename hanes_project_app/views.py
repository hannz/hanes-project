#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys

from _socket import gethostbyname, gethostname
import json
import urllib
import urllib2
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from datetime import datetime, date, timedelta
import datetime
# Create your views here.
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from forms import CaptchaForm
from django.db import models
# import eav
# from eav.models import Attribute
from hanes_project_app.models import Add_Post_Details, Menu_Category, Sub_Category, Region, Post_Images, \
    AdvertisementDetails
from captcha.models import CaptchaStore
from django.db.models import Q
#Convert months and weeks into no. of days
def date_convert(post_time,post_set_timer):
    global d
    if post_set_timer == "3 days":
        days = 3
        d = post_time + timedelta(days=days)
    if post_set_timer == "1 week":
        days = 7
        d = post_time + timedelta(days=days)
    if post_set_timer == "2 weeks":
        days = 14
        d = post_time + timedelta(days=days)
    if post_set_timer == "1 month":
        days = 1*30
        d = post_time + timedelta(days=days)
    if post_set_timer == "2 month":
        days = 2*30
        d = post_time + timedelta(days=days)
    if post_set_timer == "3 month":
        days = 3*30
        d = post_time + timedelta(days=days)
    if post_set_timer == "4 month":
        days = 4*30
        d = post_time + timedelta(days=days)
    if post_set_timer == "5 month":
        days = 5*30
        d = post_time + timedelta(days=days)
    if post_set_timer == "6 month":
        days = 6*30
        d = post_time + timedelta(days=days)
    return d

def home(request):

    advertisement_images_list = []
    advertisement_images = AdvertisementDetails.objects.all()
    for a in advertisement_images:
        ads_image = str(a.Ads_images)
        advertisement_images_list.append(ads_image)
    if request.POST:
        form = CaptchaForm(request.POST)
        if form.is_valid():
            print "ok"
    else:
        form = CaptchaForm()
    return render_to_response('home.html', dict(form=form),context_instance=RequestContext(request))

def index_view(request):

     #latest three post of arbeit menu
    Arbeit_menu_details = Add_Post_Details.objects.filter(menu_category="Arbeit").order_by('-post_time')
    i = 1
    arbeit_details_list = []
    for arbeit_details in Arbeit_menu_details:
        if i <= 3:
            temp = {}
            post_set_timer = arbeit_details.set_timer
            post_time = arbeit_details.post_time
            d = date_convert(post_time, post_set_timer)
            if date.today() <= d:
                post_id = arbeit_details.id
                post_title=arbeit_details.title
                post_description = arbeit_details.description
                post_category = arbeit_details.sub_category
                post_region = arbeit_details.region
                post_image = Post_Images.objects.filter(post_id=int(post_id))[0:1]
                if post_image:
                    for p in post_image:
                        post_image = str(p.post_image)
                else:
                    post_image = "post_images/100x100-default.png"

                temp.update({'post_id': post_id, 'post_title': post_title, 'post_description': post_description, 'post_category': post_category,'post_region': post_region,'post_image': post_image})
                arbeit_details_list.append(temp)
            else:
                continue
        else:

            break
        i = i + 1

    #latest three post of Gebrauchtes menu
    Gebrauchtes_menu_details = Add_Post_Details.objects.filter(menu_category="Gebrauchtes").order_by('-post_time')
    i = 1
    gebrauchtes_details_list = []
    for gebrauchtes_details in Gebrauchtes_menu_details:
        if i <= 3:
            temp = {}
            post_set_timer = gebrauchtes_details.set_timer
            post_time = gebrauchtes_details.post_time
            d = date_convert(post_time, post_set_timer)
            if date.today() <= d:
                post_id = gebrauchtes_details.id
                post_title = gebrauchtes_details.title
                post_description = gebrauchtes_details.description
                post_category = gebrauchtes_details.sub_category
                post_region = gebrauchtes_details.region
                post_image = Post_Images.objects.filter(post_id=post_id)[0:1]
                if post_image:
                    for p in post_image:
                        post_image = str(p.post_image)
                else:
                    post_image = "post_images/100x100-default.png"
                temp.update({'post_id': post_id, 'post_title': post_title, 'post_description': post_description,'post_image':post_image,'post_category': post_category,'post_region': post_region,})
                gebrauchtes_details_list.append(temp)
            else:
                continue
        else:

            break
        i = i + 1


    #latest three post of Produkte menu
    Produkte_menu_details = Add_Post_Details.objects.filter(menu_category="Produkte").order_by('-post_time')
    i = 1
    produkte_details_list = []
    for produkte_details in Produkte_menu_details:
        if i <= 3:
            temp = {}
            post_set_timer = produkte_details.set_timer
            post_time = produkte_details.post_time
            d = date_convert(post_time, post_set_timer)
            if date.today() <= d:
                post_id = produkte_details.id
                post_title=produkte_details.title
                post_description = produkte_details.description
                post_category = produkte_details.sub_category
                post_region = produkte_details.region
                post_image = Post_Images.objects.filter(post_id=post_id)[0:1]
                if post_image:
                    for p in post_image:
                        post_image = str(p.post_image)
                else:
                    post_image = "post_images/100x100-default.png"
                temp.update({'post_id': post_id, 'post_title': post_title, 'post_description': post_description, 'post_image': post_image, 'post_category': post_category,'post_region': post_region,})
                produkte_details_list.append(temp)
            else:
                continue
        else:

            break
        i = i + 1

    advertisement_images_list = []
    advertisement_images = AdvertisementDetails.objects.all()
    for a in advertisement_images:
        ads_image = str(a.Ads_images)
        advertisement_images_list.append(ads_image)

    advertisement_images_list = []
    verticle_ads_list = []
    advertisement_images = AdvertisementDetails.objects.all()
    for a in advertisement_images:
        ads_image = str(a.Ads_images)
        if a.ads_category == 'Bottom Image Banner':
            advertisement_images_list.append(ads_image)
        else:
            verticle_ads_list.append(ads_image)

    return render(request, 'index.html', {'arbeit_details_list':arbeit_details_list, 'gebrauchtes_details_list':gebrauchtes_details_list,'produkte_details_list':produkte_details_list, 'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})


def to_bytestring(s):
    """Convert the given unicode string to a bytestring, using the standard encoding,
    unless it's already a bytestring"""
    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf-8')

recaptcha_private_key = '6LcnlvoSAAAAAI2FgPy24xxTmpMJeXx-GrGRaztJ'  #set recaptcha private key here
recaptcha_server_name = 'http://www.google.com/recaptcha/api/verify'
recaptcha_server_form = 'https://www.google.com/recaptcha/api/challenge'


def check(client_ip_address, recaptcha_challenge_field, recaptcha_response_field):
    """Return the recaptcha reply for the client's challenge responses"""
    params = urllib.urlencode(dict(privatekey=recaptcha_private_key,
                                   remoteip=client_ip_address,
                                   challenge=recaptcha_challenge_field,
                                   response=to_bytestring(recaptcha_response_field)))
    data = None
    try:
        f = urllib2.urlopen(recaptcha_server_name, params)
        data = f.read()
        f.close()
    except urllib2.HTTPError:
        pass
    except urllib2.URLError:
        pass
    return data


def confirm(client_ip_address, recaptcha_challenge_field, recaptcha_response_field):
    """Return True/False based on the recaptcha server's reply"""
    result = False
    reply = check(client_ip_address, recaptcha_challenge_field, recaptcha_response_field)
    if reply:
        if reply.lower().startswith('true'):
            result = True
    return result


@csrf_exempt
def post_query_view(request):
    advertisement_images_list = []
    verticle_ads_list = []
    advertisement_images = AdvertisementDetails.objects.all()
    for a in advertisement_images:
        ads_image = str(a.Ads_images)
        if a.ads_category == 'Bottom Image Banner':
            advertisement_images_list.append(ads_image)
        else:
            verticle_ads_list.append(ads_image)


    all_menu_category = Menu_Category.objects.all()
    all_sub_category = Sub_Category.objects.all()
    all_region = Region.objects.all()
    form = CaptchaForm()
    menu_category_details = Menu_Category.objects.filter(menu_category="Arbeit")
    for m in menu_category_details:
        menu_id = m.id
        sub_category_details = Sub_Category.objects.filter(menu_category_id = menu_id)
    if request.POST:
        menu_category = request.POST.get('menu_category').encode('utf-8')
        sub_category = request.POST.get('sub_category')
        select_region = request.POST.get('region').encode('utf-8')
        if request.POST.get('title'):
            title = request.POST.get('title').encode('utf-8')
            if request.POST.get('description'):
                description = request.POST.get('description').encode('utf-8')
                agree = request.POST.get('agree')
                if agree == "on":
                    contact = request.POST.get('contact').encode('utf-8')
                    name = request.POST.get('name').encode('utf-8')
                    tel_no = request.POST.get('tel').encode('utf-8')
                    company_name = request.POST.get('company_name').encode('utf-8')
                    set_timer = request.POST.get('set_timer').encode('utf-8')
                    post_time = datetime.datetime.now()
                    try:

                        post_image = request.FILES['post_images'].encode('utf-8')

                    except MultiValueDictKeyError:
                        post_image = False

                    challenge_field = request.POST['recaptcha_challenge_field']
                    if request.POST['recaptcha_response_field']:
                        response_field = request.POST['recaptcha_response_field']
                        client_ip_address = gethostbyname(gethostname())
                        d = confirm(client_ip_address,
                                        recaptcha_challenge_field=challenge_field,
                                        recaptcha_response_field=response_field)
                        if d:
                            add_post_details_object = Add_Post_Details.objects.create(menu_category=menu_category,sub_category=sub_category,title=title,description=description,\
                                        contact=contact,name=name, tel=tel_no,company_name=company_name, set_timer= set_timer, post_time=post_time, region=select_region)
                            add_post_details_object.save()
                            try:
                                if request.POST.get("nof_image_field"):
                                    nof_image_field = int(request.POST.get("nof_image_field"))
                                    for i in range(nof_image_field):
                                        post_image = request.FILES[str(i+1)]
                                        Post_Images.objects.create(post=add_post_details_object,post_image=post_image)

                                else:
                                    post_image = request.FILES["1"]
                                    Post_Images.objects.create(post=add_post_details_object,post_image=post_image)
                            except MultiValueDictKeyError:
                                post_image = False
                        else:
                            error = "Captcha not match!"
                            return render(request, 'post-query.html', {'form':form,'error': error, 'selected_data':request.POST,'all_menu_category':all_menu_category,'all_sub_category':all_sub_category, 'all_region':all_region,'menu_category':'Arbeit','sub_category_details':sub_category_details,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})
                    else:
                        error = "Plz Enter Captcha!"
                        return render(request, 'post-query.html', {'form':form,'error': error, 'selected_data':request.POST,'all_menu_category':all_menu_category,'all_sub_category':all_sub_category, 'all_region':all_region,'menu_category':'Arbeit','sub_category_details':sub_category_details,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})
                else:
                    error = "Plz agree to our Terms & condition and Privacy Policy!"
                    return render(request, 'post-query.html', {'form':form,'error': error, 'selected_data':request.POST,'all_menu_category':all_menu_category,'all_sub_category':all_sub_category, 'all_region':all_region,'menu_category':'Arbeit','sub_category_details':sub_category_details,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})

            else:
                error = "Plz Enter Description!"
                return render(request, 'post-query.html', {'form':form,'error': error, 'selected_data':request.POST,'all_menu_category':all_menu_category,'all_sub_category':all_sub_category, 'all_region':all_region,'menu_category':'Arbeit','sub_category_details':sub_category_details,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})

        else:
            error = "Plz Enter Title Name!"
            return render(request, 'post-query.html', {'form':form,'error': error, 'selected_data':request.POST,'all_menu_category':all_menu_category,'all_sub_category':all_sub_category, 'all_region':all_region,'menu_category':'Arbeit','sub_category_details':sub_category_details,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})
        return HttpResponseRedirect('/index/')
    else:
        return render(request, 'post-query.html', {'form':form,'all_menu_category':all_menu_category,'all_sub_category':all_sub_category,'all_region':all_region, 'sub_category_details':sub_category_details,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})

@csrf_exempt
def sub_category_of_menu_category(request):
    if request.is_ajax():
        sub_category_list = []
        menu_category= request.POST.get('m_id')
        menu_category_data = Menu_Category.objects.filter(menu_category=menu_category)
        for m in menu_category_data:
            menu_id = m.id
            sub_category_details = Sub_Category.objects.filter(menu_category_id=menu_id)
            for s in sub_category_details:
                sub_category_list.append(s.sub_category)
        return HttpResponse(json.dumps(sub_category_list), content_type="application/json")

@csrf_exempt
def selected_menu_all_post(request, menu_category):
    advertisement_images_list = []
    verticle_ads_list = []
    advertisement_images = AdvertisementDetails.objects.all()
    for a in advertisement_images:
        ads_image = str(a.Ads_images)
        if a.ads_category == 'Bottom Image Banner':
            advertisement_images_list.append(ads_image)
        else:
            verticle_ads_list.append(ads_image)
    #Get All Post Of Selected Menu
    menu_all_post_list = []
    if Add_Post_Details.objects.filter(menu_category=menu_category):
        menu_all_post = Add_Post_Details.objects.filter(menu_category=menu_category).order_by('post_time')
        for m in menu_all_post:
            temp = {}
            post_set_timer = m.set_timer
            post_time = m.post_time
            d = date_convert(post_time, post_set_timer)
            if date.today() <= d:
                post_id = m.id
                post_title = m.title
                post_description = m.description
                post_description_short = post_description[:85] + '..'
                post_sub_category = m.sub_category
                post_selected_region = m.region
                name = m.name
                contact = m.contact
                tel = m.tel
                company_name = m.company_name
                post_date1 = str(m.post_time)
                post_date = str(datetime.datetime.strptime(post_date1, '%Y-%m-%d').strftime('%d %b.%Y'))
                #get 1 main image to display in page
                if Post_Images.objects.filter(post_id=post_id):
                    post_image_details = Post_Images.objects.filter(post_id=post_id)
                    i = 1

                    for p in post_image_details:
                        if i<=1:
                            if p.post_image:
                                post_image = p.post_image

                            else:
                                post_image=""

                        else:
                            break
                        i = i+1
                else:

                    post_image = str("post_images/100x100-default.png")

                # get Five Images To display in details page
                if Post_Images.objects.filter(post_id=post_id)[:5]:
                    first_five_images = Post_Images.objects.filter(post_id=post_id)[:5]

                else:
                    first_five_images = ""


                temp.update({'post_id': post_id, 'post_title': post_title, 'post_description': post_description,'post_description_short':post_description_short,'post_sub_category':post_sub_category,\
                             'post_selected_region':post_selected_region,'name':name, 'contact': contact, 'tel': tel, 'company_name':company_name,
                             'post_image': post_image ,'first_five_images': first_five_images,'post_date': post_date})
                menu_all_post_list.append(temp)
            else:
                continue
        menu_all_post_list = list(reversed(menu_all_post_list))
        #pagination code
        paginator = Paginator(menu_all_post_list, 10) # Show 5 contacts per page

        page = request.GET.get('page')
        try:
            menu_all_post_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            menu_all_post_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            menu_all_post_list = paginator.page(paginator.num_pages)

        #get all sub-categories and region list of selected menu
        menu_category_details = Menu_Category.objects.filter(menu_category=menu_category)
        for m in menu_category_details:
            menu_id = m.id
            sub_category_details = Sub_Category.objects.filter(menu_category_id=menu_id)

        region = Region.objects.all()
        form = CaptchaForm()
        return render(request, 'contact-detail.html', {'menu_all_post_list':menu_all_post_list,'form':form,'menu_category':menu_category, 'sub_category_details':sub_category_details, 'region':region,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list}, context_instance=RequestContext(request))

    else:
        message = "No Data Found!"
        return render(request, 'contact-detail.html', {'message':message, 'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})

@csrf_exempt
def capcha_varification_view(request):
    if request.is_ajax():
        temp = {}
        if not request.POST.get('get_captcha'):
            post_id = request.POST.get('post_id')
            challenge_field = request.POST.get('recaptcha_challenge_field')
            response_field = request.POST.get('recaptcha_response_field').upper()
            captchastore_data = CaptchaStore.objects.get(hashkey=challenge_field)
            challenge_field_new = captchastore_data.challenge
            if challenge_field_new == response_field.upper():
                message = "True"
                post_contact_details = Add_Post_Details.objects.get(id=post_id)
                name = post_contact_details.name
                contact = post_contact_details.contact
                tel = post_contact_details.tel
                company_name = post_contact_details.company_name
                temp.update({'message':message,'name': name,'contact': contact,'tel':tel,'company_name': company_name})
            else:
                message = "False"
                temp.update({'message': message})
            return HttpResponse(json.dumps(temp), content_type="application/json")
        else:
            form = CaptchaForm()
            temp.update({'form': str(form)})
            return HttpResponse(json.dumps(temp), content_type="application/json")
    else:
        print "error"

@csrf_exempt
def region_or_category_filter_view(request):
    if request.is_ajax():
        order_type = request.POST.get('order_type')
        selected_menu = request.POST.get('selected_menu')
        filtered_post_list = []
        if request.POST.get('category_list_array_stringify'):
            category_list_array = json.loads(request.POST.get('category_list_array_stringify'))
            if len(category_list_array) == 0:
                menu = Menu_Category.objects.get(menu_category=selected_menu)
                all_sub_category = Sub_Category.objects.filter(menu_category_id=menu.id)
                for s in all_sub_category:
                    category_list_array.append(s.sub_category.encode('utf-8'))

        if request.POST.get('region_list_array_stringify'):
            region_list_array = json.loads(request.POST.get('region_list_array_stringify'))
            if len(region_list_array) == 0:
                all_region = Region.objects.all()
                for r in all_region:
                    region_list_array.append(r.region.encode('utf-8'))

        if request.POST.get('search_post_title_array_stringify'):
            search_post_text = json.loads(request.POST.get('search_post_title_array_stringify'))

            if len(search_post_text) == 0:
                search_post_text = []
                all_title = Add_Post_Details.objects.filter(menu_category=selected_menu)
                for t in all_title:
                    title = t.title.encode('utf-8')
                    search_post_text.append(title)

        #get filter data by category,region and search
        if Add_Post_Details.objects.filter(sub_category__in=category_list_array, region__in=region_list_array, menu_category=selected_menu).order_by('post_time'):
            details_by_filter = Add_Post_Details.objects.filter(sub_category__in=category_list_array, region__in=region_list_array, menu_category=selected_menu)
            details_by_filter = details_by_filter.order_by('-post_time')
            for s in search_post_text:
                details_by_all_filter = details_by_filter.filter(Q(title__icontains=str(s))) or details_by_filter.filter(Q(description__icontains=str(s)))
                for dc in details_by_all_filter:
                    five_post_images_list = []
                    temp = {}
                    post_set_timer = dc.set_timer
                    post_time = dc.post_time
                    d = date_convert(post_time, post_set_timer)
                    if date.today() <= d:
                        post_id = dc.id
                        post_title = dc.title
                        post_description = dc.description
                        post_description_short = post_description[:85] + '..'
                        post_sub_category = dc.sub_category
                        post_selected_region = dc.region
                        post_date1 = str(dc.post_time)
                        post_date = str(datetime.datetime.strptime(post_date1, '%Y-%m-%d').strftime('%d %b.%Y'))
                        name = dc.name
                        contact = dc.contact
                        tel = dc.tel
                        company_name = dc.company_name
                        form = CaptchaForm()

                        #get 1 main image to display in page
                        if Post_Images.objects.filter(post_id=post_id):

                            post_image_details = Post_Images.objects.filter(post_id=post_id)
                            i = 1

                            for p in post_image_details:
                                if i<=1:
                                    if p.post_image:
                                        post_image = str(p.post_image)
                                    else:
                                        post_image= ""

                                else:
                                    break
                                i =i+1
                        else:

                            post_image = "post_images/100x100-default.png"

                        if Post_Images.objects.filter(post_id=post_id):

                            post_image_details = Post_Images.objects.filter(post_id=post_id)
                            i = 1

                            for p in post_image_details:
                                if i<=5:
                                    if p.post_image:
                                        five_post_image = str(p.post_image)
                                        five_post_images_list.append(five_post_image)

                                    else:
                                        five_post_image= ""
                                else:
                                    break
                                i = i+1
                        else:

                            five_post_image = ""

                        temp.update({'post_id': post_id, 'form': str(form),'post_title': post_title, 'post_description': post_description, 'post_description_short':post_description_short,'post_sub_category': post_sub_category,\
                                     'post_selected_region':post_selected_region,'name': name, 'contact': contact, 'tel': tel,'company_name': company_name,'post_date':post_date,\
                                     'post_image': post_image, 'five_post_images_list': five_post_images_list})
                        filtered_post_list.append(temp)

                    else:
                        continue
        if order_type == "ascending":
            filtered_post_list.sort(key=lambda temp: datetime.datetime.strptime(temp['post_date'], "%d %b.%Y"), reverse=True)
        else:
            filtered_post_list.sort(key=lambda temp: datetime.datetime.strptime(temp['post_date'], "%d %b.%Y"), reverse=False)
        return HttpResponse(json.dumps(filtered_post_list), content_type="application/json")
    else:
        print "error"

@csrf_exempt
def post_by_menu_post_title(request, post_title):
    advertisement_images_list = []
    verticle_ads_list = []
    advertisement_images = AdvertisementDetails.objects.all()
    for a in advertisement_images:
        ads_image = str(a.Ads_images)
        if a.ads_category == 'Bottom Image Banner':
            advertisement_images_list.append(ads_image)
        else:
            verticle_ads_list.append(ads_image)


    #Get Post Of Selected Title]
    menu_all_post_list = []
    if Add_Post_Details.objects.filter(title=post_title):
        menu_all_post = Add_Post_Details.objects.filter(title=post_title)

        for m in menu_all_post:

            temp = {}
            post_id = m.id
            post_title = m.title
            post_description = m.description
            post_description_short = post_description[:85] + '..'
            post_sub_category = m.sub_category
            post_selected_region = m.region
            name = m.name
            contact = m.contact
            tel = m.tel
            company_name = m.company_name
            menu_category = m.menu_category
            post_date1 = str(m.post_time)
            post_date = str(datetime.datetime.strptime(post_date1, '%Y-%m-%d').strftime('%d %b.%Y'))
            #get 1 main image to display in page
            if Post_Images.objects.filter(post_id=post_id):
                post_image_details = Post_Images.objects.filter(post_id=post_id)
                i = 1

                for p in post_image_details:
                    if i<=1:
                        if p.post_image:
                            post_image = p.post_image

                        else:
                            post_image = "post_images/100x100-default.png"

                    else:
                        break
                    i = i+1
            else:

                post_image = "post_images/100x100-default.png"

            # get Five Images To display in details page

            if Post_Images.objects.filter(post_id=post_id)[:5]:
                first_five_images = Post_Images.objects.filter(post_id=post_id)[:5]

            else:
                first_five_images = ""


            temp.update({'post_id': post_id, 'post_title': post_title, 'post_description': post_description,'post_description_short':post_description_short,'post_sub_category':post_sub_category,\
                         'post_selected_region':post_selected_region,'name':name, 'contact': contact, 'tel': tel, 'company_name':company_name,
                         'post_image': post_image, 'first_five_images': first_five_images,'post_date':post_date})
            menu_all_post_list.append(temp)


        #get all sub-categories and region list of selected menu
        menu_category_details = Menu_Category.objects.filter(menu_category=menu_category)
        for m in menu_category_details:
            menu_id = m.id
            sub_category_details = Sub_Category.objects.filter(menu_category_id =menu_id)

        region = Region.objects.all()
        form = CaptchaForm()
        menu_all_post_list = list(reversed(menu_all_post_list))
        return render(request, 'contact-detail.html', {'form': form, 'menu_all_post_list':menu_all_post_list,'menu_category':menu_category, 'sub_category_details':sub_category_details, 'region':region, 'post_title': post_title,'ads_image':advertisement_images_list,'verticle_ads_list':verticle_ads_list})

    else:
        message = "No Data Found!"
        return render(request, 'contact-detail.html', {'message':message, 'ads_image':advertisement_images_list, 'verticle_ads_list':verticle_ads_list})

@csrf_exempt
def all_post_by_search(request):
    if request.is_ajax():
        search_post_text = request.POST.get('search_post_text')
        if search_post_text != "":
            if Add_Post_Details.objects.filter(title__istartswith=search_post_text):
                menu_search_post_title_dict = {}
                menu_search_post_title_list = []
                menu_search_post_title = Add_Post_Details.objects.filter(title__istartswith=search_post_text)
                for m in menu_search_post_title:
                    temp = {}
                    post_set_timer = m.set_timer
                    post_time = m.post_time
                    d = date_convert(post_time, post_set_timer)
                    if date.today() <= d:
                        post_id = m.id
                        post_title = m.title.encode('utf-8')
                        temp.update({'post_id': post_id, 'post_title': post_title})
                        menu_search_post_title_list.append(temp)
                    else:
                        continue
                menu_search_post_title_dict.update({'menu_search_post_title_list': menu_search_post_title_list})
                return HttpResponse(json.dumps(menu_search_post_title_dict), content_type="application/json")

            else:
                message = "No Any Record Found!"
                return HttpResponse(json.dumps(message), content_type="application/json")

        else:
            message = "Plz Enter Text!"
        return HttpResponse(json.dumps(message), content_type="application/json")
    else:
        print "error"


@csrf_exempt
def add_advertise(request):
    if request.POST:
        try:
            ads_category = request.POST['ads_category']
            if request.FILES['select_ads']:
                advertise_image = request.FILES['select_ads']
                if not AdvertisementDetails.objects.filter(ads_category=ads_category).exists():
                    AdvertisementDetails.objects.create(ads_category=ads_category, Ads_images=advertise_image)
                else:
                    AdvertisementDetails.objects.filter(ads_category=ads_category).delete()
                    AdvertisementDetails.objects.create(ads_category=ads_category, Ads_images=advertise_image)
                return render(request, 'admin/enter_adverisement_image.html', {'message':"Image Uploded!"})

            else:
                return render(request, 'admin/enter_adverisement_image.html', {'error':"Plz Select Image!"})

        except MultiValueDictKeyError:
            advertise_image = False
        return render(request, 'admin/enter_adverisement_image.html',{})


    else:
        return render(request, 'admin/enter_adverisement_image.html', {})




