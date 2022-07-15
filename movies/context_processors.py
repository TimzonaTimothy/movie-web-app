from .models import MoviesCategory

def menu_links(request):
    links = MoviesCategory.objects.all()
    return dict(links=links)