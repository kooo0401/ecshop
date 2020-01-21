from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # big = ImageSpecField(source="origin",
    # processors=[ResizeToFill(1280, 1024)],
    # format='JPEG'
    # )

    # thumbnail = ImageSpecField(source='origin',
    #     processors=[ResizeToFill(250,250)],
    #     format="JPEG",
    #     options={'quality': 60}
    # )

    # middle = ImageSpecField(source='origin',
    #     processors=[ResizeToFill(600, 400)],
    #     format="JPEG",
    #     options={'quality': 75}
    # )

    # small = ImageSpecField(source='origin',
    #     processors=[ResizeToFill(75,75)],
    #     format="JPEG",
    #     options={'quality': 50}
    # )


    class Meta:
        ordering = ('-id',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)