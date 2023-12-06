# i want to make categories available to all templates so i will put
# 'store.views.categories' in settings.py ('context_processors')
from .models import Category


def categories(request):
    return {"categories": Category.objects.all()}
