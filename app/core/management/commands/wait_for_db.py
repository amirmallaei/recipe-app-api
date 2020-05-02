import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause excetion until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('w8ing for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('database unavailable. hold on a sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available'))
