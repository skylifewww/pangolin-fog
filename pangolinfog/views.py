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
from django.http import HttpResponseRedirect
from pangolinfog.forms import *
# from pangolinfog.recaptcha.forms import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from product.models import Category
from product.models import Product, Accessory
from content.models import Slide
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from nocaptcha_recaptcha.fields import NoReCaptchaField


def contact(request):

    form_class = ContactForm
    success_url = reverse_lazy('success')

    args = {}
    background_image = get_object_or_404(Slide, header_about=1)
    args['menu'] = "contact"
    categories_main_menu = Category.objects.filter(published_in_menu=1).order_by('ordering')
    args['categories_main_menu'] = categories_main_menu
    args['form'] = form_class
    args['background_image'] = background_image

    def form_valid(self, form):
        return super(form_class, self).form_valid(form)

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_phone = request.POST.get(
                'contact_phone'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "Pangolin Fog",
                content,
                "Pangolin Fog" +'',
                ['vladimir@pangolin.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'contact.html', args) 


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



