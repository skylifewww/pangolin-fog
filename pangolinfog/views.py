import os
from django.http import FileResponse
from wsgiref.util import FileWrapper
from settings.static import MEDIA_URL
# from django.core.servers.basehttp import FileWrapper
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from pangolinfog.forms import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from product.models import Category
from product.models import Product
from content.models import Slide



def jq_subsc(request):
   
    return render(request, 'jq_subsc.html')


def download_file(request):
    _file = 'manualtourhazer2.pdf.zip'
    filename = os.path.basename(_file)

    # python 3
    # response = FileResponse(FileWrapper(open(filename, 'rb')), content_type='application/x-zip-compressed')

    # python 2
    response = FileResponse(FileWrapper(file(filename, 'rb')), content_type='application/x-zip-compressed')
     
    
    response['Content-Disposition'] = "attachment; filename=%s" % _file
    return response


def download_mp3(request):
    _file = 'Last_Summer_in_Yalta.mp3.zip'
    filename = os.path.basename(_file)

    # python 3
    # response = FileResponse(FileWrapper(open(filename, 'rb')), content_type='application/x-zip-compressed')

    # python 2
    response = FileResponse(FileWrapper(file(filename, 'rb')), content_type='application/x-zip-compressed')
     
    
    response['Content-Disposition'] = "attachment; filename=%s" % _file
    return response    


def main(request):
	args = {}
	slides = Slide.objects.filter(published_main=1).order_by('ordering')
	categories_main_menu = Category.objects.filter(published_in_menu=1).order_by('ordering')
	products_main = Product.objects.filter(published_main=1)
	args['products_main'] = products_main
	args['categories_main_menu'] = categories_main_menu
	args['slides'] = slides

	return render_to_response("home.html", args)


    
def news(request):

	args = {}
	
	slides = Slide.objects.filter(published_portfolio=1).order_by('ordering')
	news = Slide.objects.filter(published_news=1).order_by('ordering')
	background_image = get_object_or_404(Slide, header_about=1)


	args['news'] = news
	args['menu'] = "news"
	args['slides'] = slides
	args['background_image'] = background_image

	return render_to_response("news.html", args)


def about(request):

	args = {}
	slides = Slide.objects.filter(published_portfolio=1).order_by('ordering')
	news = Slide.objects.filter(published_news=1).order_by('ordering')
	background_image = get_object_or_404(Slide, header_about=1)


	args['news'] = news
	args['menu'] = "about"
	args['slides'] = slides
	args['background_image'] = background_image

	return render_to_response("about.html", args)




def contact(request):

	args = {}
	args['menu'] = "contact"
	categories_main_menu = Category.objects.filter(published_in_menu=1).order_by('ordering')
	args['categories_main_menu'] = categories_main_menu

	return render_to_response("contact.html", args)


