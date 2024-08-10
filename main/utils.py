from django.db.models import Q

from main.models import Shoes
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank


def g_search(query):
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    return Shoes.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')

    # return Shoes.objects.filter(description__search=query)

    # if len(query.split()) == 1:
    #     keywords = query.split()
    # else:
    #     keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_obj = Q()
    # for token in keywords:
    #     q_obj |= Q(name__icontains=token)
    #     q_obj |= Q(description__icontains=token)
    #
    # return Shoes.objects.filter(q_obj)
