from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
import random
from .models import ListItem
from datetime import datetime

ids_of_selected_items = []


def select_items(request):
    if request.method == 'POST':
        global ids_of_selected_items
        ids_selected = request.POST.getlist('items[]')
        ids_of_selected_items = ids_selected
    return JsonResponse({"response": "ok"})


def show_selected(request):
    items = ListItem.objects.filter(id__in=ids_of_selected_items)
    return render(request, 'selected.html', context={"items": items})


def add_data(request):
    word_size = random.randint(10, 15)
    limit = 200
    for i in range(limit):
        word = ""
        for j in range(word_size):
            word += chr(random.randint(65, 90))
        ListItem.objects.create(name=word, date_added=datetime.today())
    return JsonResponse({"response": "ok"})


def delete_data(request):
    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('items[]')
        for id in ids_to_delete:
            id = int(id.split(" ")[0])
            ListItem.objects.get(id=id).delete()
    return JsonResponse({"response": "ok"})


def delete_all(request):
    ListItem.objects.all().delete()
    return JsonResponse({"response": "ok"})


def list_items(request):
    list_of_items = ListItem.objects.all()
    paginator = Paginator(list_of_items, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = serializers.serialize('json', page_obj)
    return JsonResponse({"page_obj": data, "total_pages": page_obj.paginator.num_pages})


def index(request):
    return render(request, "home.html")
