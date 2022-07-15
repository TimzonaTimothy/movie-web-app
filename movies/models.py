from django.db import models

# Create your models here.

class MoviesCategory(models.Model):
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/movies/categories', blank=True)


    class Meta:
        verbose_name = 'movie category'
        verbose_name_plural = 'movie categories'
        

    # def get_url(self):
    #     return reverse('product_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name


class Movies(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(MoviesCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)
    video = models.FileField(upload_to='video/movies/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
        ordering = ['-created_at']