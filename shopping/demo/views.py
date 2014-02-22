from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from demo.models import ItemToBuy, ItemToBuySerializer, CATEGORIES


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({'CATEGORIES': [a[0] for a in CATEGORIES]})
        return context

class ItemList(generics.ListCreateAPIView):
	'''
	API endpoint that represnts a list of items to buy.
	'''
	model = ItemToBuy
	serializer_Class = ItemToBuySerializer

# generics.RetrieveAPIView
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	'''
	API endpoint that represnts
	'''
	model = ItemToBuy