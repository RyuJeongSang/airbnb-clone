from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 2)
    rooms = paginator.get_page(page)

    page_numbers_range = 10

    max_index = rooms.paginator.num_pages
    start_index = int((page - 1) / page_numbers_range) * page_numbers_range
    print(start_index)
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    return render(
        request,
        "rooms/home.html",
        {"rooms": rooms, "paginator_range": paginator_range},
    )
