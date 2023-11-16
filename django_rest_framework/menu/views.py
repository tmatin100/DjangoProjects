from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Item 
from .serializers import ItemSerializer


# Create your views here.

"""def item_list(request):
    # QueryObject => Python list[dicts]         # chaning query obects to python list[dictinoaries]
    # We can do this with django out of the box, with a serializer (serializers.py file )
    items = Item.objects.all()    
    item_list = []
    for item in items:
        item_list.append({
            "name": item.name, 
            "price": item.price, 
            "description": item.description, 

        })
    # return HttpResponse(items)
    return JsonResponse({"menu_items": item_list})  # returns a json fomrat 
"""

@api_view(['Get'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


# Serialzion - a process of changing one datatype to another data type.   ex. list to dictionary     
def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True) #specify if there will be many items or single items 
    return JsonResponse(serializer.data, safe=False) # access and return the seralized dato into jason sresponse 

@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)    # retreives individual object by the pk (primary key)
    serializer = ItemSerializer(item)  # many item is false by default 
    return Response(serializer.data)