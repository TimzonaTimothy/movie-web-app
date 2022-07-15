from django.db import models

# Create your models here.

class TrailerCategory(models.Model):
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/trailer/categories', blank=True)


    class Meta:
        verbose_name = 'trailer category'
        verbose_name_plural = 'trailer categories'


    # def get_url(self):
    #     return reverse('product_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name


class Trailer(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(TrailerCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)
    video = models.FileField(upload_to='video/trailer/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'trailer'
        verbose_name_plural = 'trailer'
        ordering = ['-created_at']