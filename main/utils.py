from django.db.models import Q

from main.models import Shoes


def g_search(query):

    keywords = [word for word in query.split() if len(word) > 2]
    q_obj = Q()
    for token in keywords:
        q_obj |= Q(name__icontains=token)

    return Shoes.objects.filter(q_obj)
