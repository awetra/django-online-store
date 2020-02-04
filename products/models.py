from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.text import slugify


def image_directory_path(image, image_name):
    return f'products/{image.product.name}/{image_name}'


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('products_list_by_category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(null=True, blank=True, default=0)

    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return f'{self.name} | {self.price}$'

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')
        if not self.discount < 100:
            raise ValidationError('Discount must be less than 100.')

    def get_absolute_url(self):
        return reverse(
            'product_detail', 
            kwargs={
                'category_slug': self.category.slug,
                'product_slug': self.slug
            }
        )


class Image(models.Model):
    upload = models.ImageField(upload_to=image_directory_path)
    is_main = models.BooleanField(null=True, blank=True, default=False)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return self.product.name

    def save(self, **kwargs):
        if not self.product.images.count():
            self.is_main = True
        elif not self.id and self.is_main:
            previous_main_image = Image.objects.get(product=self.product, is_main=True)
            previous_main_image.is_main = False
            previous_main_image.save()

        super().save(**kwargs)

    def clean(self):
        pass
        # if self.id and not self.is_main and self.product.images.filter(is_main=True).count() == 1:
        #     raise ValidationError('Must be the main image.')


class Comment(models.Model):
    text = models.TextField()
    rating = models.PositiveIntegerField(null=True, blank=True, default=0)

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return f'{self.customer.email}|{self.product.name}'
