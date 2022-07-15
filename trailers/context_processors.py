from .models import TrailerCategory

def menu_links(request):
    links = TrailerCategory.objects.all()
    return dict(links=links)