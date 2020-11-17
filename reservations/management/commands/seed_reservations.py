import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations.models import Reservation
from rooms.models import Room
from users.models import User


NAME = "reservations"


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
            Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))