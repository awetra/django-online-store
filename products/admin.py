from django.contrib import admin

from .models import Category, Product, Image, Comment


admin.site.register(Image)
admin.site.register(Comment)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    excludes = ('slug',)
    inlines = [ImageInline, CommentInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)