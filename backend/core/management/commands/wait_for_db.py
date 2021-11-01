# Створення файлу з командами для manage.py


import time
from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError

# Команда, щоб при compose БД в докері система не видавала повідомлення,
# що вона не змогла приєднатися до БД
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('waiting for db...')
        db_con = False
        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Database is unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available!!!')) # вказання в Style конкретного типу  шрифту для серверу:

