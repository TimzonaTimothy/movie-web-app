from .models import SeasonalCategory

def menu_links(request):
    links = SeasonalCategory.objects.all()
    return dict(links=links)