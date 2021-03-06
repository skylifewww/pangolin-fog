# -*- coding: utf-8 -*-  

from django.contrib.auth.models import User
# from iosDevCourse.users.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import mptt
from mptt.fields import TreeForeignKey
import random
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField
# from content.models import Slide


def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    c = filename.split(".")
    filename = str(n1) + "_" + str(n2) + "_" + str(n3) + "." + c[-1]
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=250, verbose_name="Name Category", blank=True, default="", unique=True)
    parent = TreeForeignKey('self', related_name="children", blank=True, null=True, db_index=True, verbose_name="Parent class")
    published = models.BooleanField(verbose_name="Published", blank=True, default="")
    published_in_menu = models.BooleanField(verbose_name="Published in main menu", default="", blank=True)
    published_in_second = models.BooleanField( blank=True, default="", verbose_name="Published in second menu")
    published_in_products = models.BooleanField( blank=True, default="", verbose_name="Published in all products")
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)

    def get_slides(self):
        return Slide.objects.filter(category=self)

    def get_products(self):
        return Product.objects.filter(product_category=self)        

    def get_parent(self):
        return self.parent    

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('tree_id','level')

    def __str__(self):
        return self.name

    class MPTTMeta:
        # level_attr = 'mptt_level'
        order_insertion_by = ['name']    


mptt.register(Category, order_insertion_by=['name'])




class Creator(MPTTModel):
    slug = models.CharField(max_length=250, blank=True, verbose_name="Url")
    name = models.CharField(max_length=200, verbose_name="Creator device", blank=True, default="", unique=True)
    parent = TreeForeignKey('self', related_name="children", blank=True, null=True, db_index=True, verbose_name="Parent class")

    class Meta:
        db_table = "creators"
        verbose_name = "Creator"
        verbose_name_plural = "Creators"
        ordering = ('tree_id', 'level')

    def __str__(self):
        return self.name

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = 'Logo Creator'
    pic_slug.allow_tags = True       

    class MPTTMeta:
        # level_attr = 'mptt_level'
        order_insertion_by = ['name']    


mptt.register(Creator, order_insertion_by=['name'])


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name="Tag Name")

    class Meta:
        db_table = "tags"
        verbose_name = "tags"
        verbose_name_plural = "tag"

    def __str__(self):
        return self.tag_name


# class Works(models.Model):
#     work_creator = models.CharField(max_length=50, verbose_name="creator", blank=True, null=True, default="")
#     work_category = TreeForeignKey(Category, related_name="works", verbose_name="Category", default="", blank=True)
#     # image = ThumbnailerImageField(upload_to=make_upload_path, blank=True, verbose_name="картинка")
#     slug = models.CharField(max_length=250, blank=True, verbose_name="Url")
#     short_text = RichTextUploadingField(blank=True, verbose_name="Short text")
#     full_text = RichTextUploadingField(blank=True, verbose_name="Full text")
#     work_title = models.CharField(max_length=50, verbose_name="Work Title")

#     class Meta:
#         db_table = "works"
#         verbose_name = "works"
#         verbose_name_plural = "works"

#     def __unicode__(self):
#         return self.work_title

    # def pic(self):
    #     if self.image:
    #         return u'<img src="%s" width="70"/>' % self.image.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True 

    # def pic_slug(self):
    #     if self.slug:
    #         return u'<img src="%s" width="70"/>' % self.slug
    #     else:
    #         return '(none)'
    # pic_slug.short_description = 'work'
    # pic_slug.allow_tags = True                  


class Product(models.Model):
    product_title = models.CharField(max_length=250, verbose_name="Product Title")
    product_date = models.DateTimeField(verbose_name="Release date")
    product_tag = models.ManyToManyField(Tag, related_name="tags", related_query_name="tags", verbose_name="Tags")
    # product_works = models.ManyToManyField(Works, related_name="works", related_query_name="works", verbose_name="Works", blank=True, default="")
    product_category = TreeForeignKey(Category, related_name="products", verbose_name="Categories", default="", blank=True)
    product_creator = TreeForeignKey(Creator, related_name="creator", max_length=200, verbose_name="Creator", blank=True, default="")
    product_image = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name="Image")
    product_video = EmbedVideoField(verbose_name='Video', blank=True, help_text='URL video', null=True)
    product_price = models.FloatField(verbose_name="Price", default=0, blank=True, null=True)
    video_published = models.BooleanField( blank=True, default="")
    slug_small = models.CharField(max_length=250, blank=True, verbose_name="Slug_Small")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Slug")
    slogan = models.CharField(max_length=250, verbose_name="Product Slogan")
    short_text = RichTextUploadingField(blank=True, verbose_name="Short text")
    full_text = RichTextUploadingField(blank=True, verbose_name="Full text")
    published = models.BooleanField(verbose_name="Published", blank=True)
    published_main = models.BooleanField( blank=True, default="", verbose_name="Published on main page")
    no_published_in_all = models.BooleanField( blank=True, default="", verbose_name="Do not Published on All products")
    related_products = models.BooleanField( blank=True, default="", verbose_name="Published on product page")
    related_title = models.CharField(max_length=250,  default="", blank=True, verbose_name="Related Product Title")
    related_category = models.ManyToManyField(Category, related_name="related", related_query_name="related", blank=True, verbose_name="Related Category")
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)

    def get_accessories(self):      
        return Accessory.objects.filter(category__name__exact=self.product_category)    

    def get_overviews(self):
        return Overview.objects.filter(category=self.product_category, published=1)        

    def get_techSpecs(self):
        return TechSpec.objects.filter(product=self, published=1)     

    def get_slides(self):
        return SlideProduct.objects.filter(category=self.product_category, published_portf=1) 

    def get_bg_slide(self):
        return SlideProduct.objects.get(category=self.product_category, published_bg=1)

    # def get_related(self):
        # return Product.objects.filter(product_category__in=self.related_category.get_descendants(include_self=True), related_products=1)
                   # Article.objects.filter(article_tag__tag_name__exact=current_tag)

    def __str__(self):
        return self.product_title

    class Meta:
        db_table = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['ordering']

    def pic(self):
        if self.product_image:
            return u'<img src="%s" width="70"/>' % self.product_image.url
        else:
            return '(none)'
    pic.short_description = 'Product image'
    pic.allow_tags = True  

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = 'Product image slug'
    pic_slug.allow_tags = True

    def pic_slug_small(self):
        if self.slug_small:
            return u'<img src="%s" width="70"/>' % self.slug_small
        else:
            return '(none)'
    pic_slug_small.short_description = 'Product image small'
    pic_slug_small.allow_tags = True  
 


class MenuItemProduct(models.Model):
    category = models.ManyToManyField(Category, related_name="menuitem", related_query_name="menuit", blank=True, verbose_name="Category")
    name = models.CharField(max_length=200, verbose_name="Name")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Url")
    published = models.BooleanField(verbose_name="Published")
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menuItemsProducts'
        verbose_name_plural = "Menu Items for Products"
        verbose_name = "Menu Item"
        ordering = ['ordering']


class Overview(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="Category")
    name = models.CharField(max_length=200, verbose_name="Name")
    text = RichTextUploadingField(blank=True, verbose_name="Text")
    icon = models.CharField(max_length=250, blank=True, verbose_name="Icon")
    published = models.BooleanField(verbose_name="Published")
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'overviews'
        verbose_name_plural = "Overviews"
        verbose_name = "Overview"
        ordering = ['ordering'] 



class Accessory(models.Model):
    category = models.ManyToManyField(Category, related_name="accessories", related_query_name="access", blank=True, verbose_name="Category")
    name = models.CharField(max_length=200, verbose_name="Name")
    slogan = models.CharField(max_length=250, verbose_name="Accessory Slogan")
    image = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name="Image")
    text = RichTextUploadingField(blank=True, verbose_name="Text")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Pic")
    price = models.FloatField(verbose_name="Price", default=0, blank=True, null=True)
    published = models.BooleanField(verbose_name="Published")
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'accessories'
        verbose_name_plural = "Accessories"
        verbose_name = "Accessory"
        ordering = ['ordering'] 

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = 'Accessory image slug'
    pic_slug.allow_tags = True   

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = 'Accessory image'
    pic.allow_tags = True                    
        
    

class TechSpec(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, verbose_name="Product")
    name = models.CharField(max_length=200, verbose_name="Name")
    text1 = RichTextUploadingField(blank=True, verbose_name="Text1")
    text2 = RichTextUploadingField(blank=True, verbose_name="Text2")
    text3 = RichTextUploadingField(blank=True, verbose_name="Text3")
    published = models.BooleanField(verbose_name="Published")
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'techSpecs'
        verbose_name_plural = "TechSpecs"
        verbose_name = "TechSpec"
        ordering = ['ordering']    



class Support(models.Model):
    title = models.CharField(max_length=250, verbose_name="Support Title")
    # date = models.DateTimeField(verbose_name="Release date")
    tag = models.ManyToManyField(Tag, related_name="support_tags", related_query_name="support_tags", verbose_name="Tags")
    # product_works = models.ManyToManyField(Works, related_name="works", related_query_name="works", verbose_name="Works", blank=True, default="")
    category = TreeForeignKey(Category, related_name="supports", verbose_name="Categories", default="", blank=True)
    # product_creator = TreeForeignKey(Creator, related_name="creator", max_length=200, verbose_name="Creator", blank=True, default="")
    video = EmbedVideoField(verbose_name='Video', blank=True, help_text='URL video', null=True)
    video_published = models.BooleanField( blank=True, default="")
    image = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name="Image")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Url")
    slogan = models.CharField(max_length=250, verbose_name="Support Slogan")
    short_text = RichTextUploadingField(blank=True, verbose_name="Short text")
    full_text = RichTextUploadingField(blank=True, verbose_name="Full text")
    published = models.BooleanField(verbose_name="Published", blank=True)
    # published_main = models.BooleanField( blank=True, default="", verbose_name="Published on main page",)
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)
    
    
   

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'support'
        verbose_name = "Support"
        verbose_name_plural = "Supports"
        ordering = ['ordering']

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = 'Support image'
    pic.allow_tags = True  

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = 'Support image slug'
    pic_slug.allow_tags = True     

    

class SlideProduct(models.Model):
    category = models.ForeignKey(Category, related_name="slideproduct", verbose_name="Category", default="", blank=True, null=True)
    name = models.CharField(max_length=250, verbose_name="Name")
    image = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name="Image")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Url pic")
    text1 = RichTextUploadingField(blank=True, verbose_name="Text1")
    text2 = RichTextUploadingField(blank=True, verbose_name="Text2")
    published_bg = models.BooleanField(verbose_name="Published as BG", blank=True, default=0)
    published_portf = models.BooleanField(verbose_name="Published in Portfolio", blank=True, default=0)
    published_in_all = models.BooleanField(verbose_name="Published in All Products", blank=True, default=0)
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)
    
        
    def __str__(self):
        return self.name

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = 'Slide'
    pic.allow_tags = True

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = 'Slide slug'
    pic_slug.allow_tags = True   

    class Meta:
        # db_table = 'slide_products'
        verbose_name_plural = "Slides"
        verbose_name = "Slide" 
        ordering = ['ordering'] 
    





