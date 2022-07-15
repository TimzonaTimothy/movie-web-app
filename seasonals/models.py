from django.db import models

# Create your models here.

class SeasonalCategory(models.Model):
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/seasonal/categories', blank=True)


    class Meta:
        verbose_name = 'seasonal category'
        verbose_name_plural = 'seasonal categories'
        


    # def get_url(self):
    #     return reverse('product_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name




class Seasonal(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(SeasonalCategory, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'seasonal'
        verbose_name_plural = 'seasonals'
        ordering = ['-created_at']


class Episode(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    season = models.ForeignKey(Seasonal, on_delete=models.CASCADE, related_name='season')
    description = models.CharField(max_length=1000, blank=True)
    video = models.FileField(upload_to='video/seasonal/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        ordering = ['-created_at']