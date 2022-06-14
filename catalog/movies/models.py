from distutils.command.upload import upload
from sre_constants import CATEGORY
from tabnanny import verbose
from unicodedata import category
from django.db import models
from matplotlib import image
from pandas import describe_option

# Create your models here.
CATEGORY_CHOICES = (
    ('A','AKSİYON'),
    ('M','MACERA'),
    ('B','BİLİM-KURGU'),
    ('A','ANİMASYON'),
    ('B','BİYOGRAFİ'),
)

STATUS_CHOICES = (
    ('EY','En Yeniler'),
    ('P','Popüler'),
    ('ÖÇ','Öne Çıkan'),
)


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Film Adı')
    description = models.TextField(verbose_name='Film Açıklaması')
    image = models.TextField(verbose_name='Film Afişi')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image