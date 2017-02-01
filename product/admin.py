from django.contrib import admin
from product.models import *
from embed_video.admin import AdminVideoMixin
from mptt.admin import MPTTModelAdmin
from product.fields import AdminImageWidget
from easy_thumbnails.fields import ThumbnailerImageField


# Register your models here.
class OverviewInline(admin.StackedInline):
    model = Overview
    extra = 1

class TechSpecInline(admin.StackedInline):
    model = TechSpec
    extra = 3


class SlideProductInline(admin.StackedInline):
    model = SlideProduct
    extra = 5
    formfield_overrides = {
        ThumbnailerImageField: {'widget': AdminImageWidget},
    }         

class ProductAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ["product_title", "product_creator", "product_video", 'video_published', "product_date", "slogan", "product_price", 'short_text',
              'full_text', "product_image", 'slug',
              "product_tag", "product_category", 'published', 'ordering', 'published_main', 'related_products', 'related_category']

   
    list_filter = ["product_title", "product_date", "product_tag", "product_category", "product_creator", 'published']
    search_fields = ["product_title", "product_date", "product_tag", "product_category", "product_creator"]
    list_display = ["product_title", "product_price", "product_category", "product_creator", 'published', 'ordering', 'published_main', 'pic', 'pic_slug', 'related_products', 'related_category']
    list_editable = ['published', "product_price", 'ordering', 'published_main', 'related_products', 'related_category']
    inlines = [TechSpecInline]

    formfield_overrides = {
        ThumbnailerImageField: {'widget': AdminImageWidget},
    }

class AccessoryAdmin(admin.ModelAdmin):
    list_filter = ["name", "category"]
    search_fields = ["name"]
    list_display = ["name", 'published', 'ordering', 'pic', 'pic_slug', "price"]
    list_editable = ['published', 'ordering', "price"]
    formfield_overrides = {
        ThumbnailerImageField: {'widget': AdminImageWidget},
    }    

class MenuItemProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['category', 'name', 'slug', 'published', 'ordering']
    list_editable = ['slug', 'published', 'ordering']


class OverviewAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'icon', 'published', 'ordering']
    list_editable = ['published', 'ordering']


class TechSpecAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'published', 'ordering']
    list_editable = ['published', 'ordering']


class SupportAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ["title", "video", 'video_published', "slogan", 'short_text',
              'full_text',"image", 'slug',
              "tag", "category", 'published', 'ordering']

   
    list_filter = ["title", "tag", "category", 'published']
    search_fields = ["title", "tag", "category"]
    list_display = ["title", "category", 'published', 'ordering', 'pic', 'pic_slug']
    list_editable = ['published', 'ordering']
    formfield_overrides = {
        ThumbnailerImageField: {'widget': AdminImageWidget},
    }


class  CategoryAdmin(admin.ModelAdmin):
      # fields = ['name', 'parent']
      list_display = ['name', 'parent', 'published', 'published_in_menu', 'published_in_second', 'ordering']
      list_editable = ['published', 'ordering', 'published_in_second', 'published_in_menu']
      inlines = [OverviewInline, SlideProductInline]


class  CreatorAdmin(admin.ModelAdmin):
      list_display = ['name', 'pic_slug']      




class SlideProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'pic', 'pic_slug', 'category', 'published_bg', "published_portf", 'ordering']
    list_editable = ['published_bg','ordering', "published_portf"]
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

   
       
admin.site.register(Product, ProductAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Overview, OverviewAdmin)
admin.site.register(SlideProduct, SlideProductAdmin)
admin.site.register(TechSpec, TechSpecAdmin)
admin.site.register(Support, SupportAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(MenuItemProduct, MenuItemProductAdmin)
admin.site.register(Tag)
# admin.site.register(Works, WorksAdmin)
