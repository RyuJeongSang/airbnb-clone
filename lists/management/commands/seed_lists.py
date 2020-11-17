import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from rooms.models import Room
from users.models import User


NAME = "lists"


class Command(BaseCommand):

    help = "creates lists command"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="how many lists do you want to"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        rooms = Room.objects.all()
        users = User.objects.all()
        seeder.add_entity(
            List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        creat_rooms = seeder.execute()
        cleaned = flatten(list(creat_rooms.values()))
        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 10)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} Lists created"))