from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "creates facilities command"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created"))
