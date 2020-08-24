import os, sys, django, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hince.settings")
django.setup()

from store.models import Store

CSV_PATH = '/home/taehyun/Wecode/11-Hipce-backend/crawling/store_crawling.csv'

with open(CSV_PATH) as f:
    drd = csv.reader(f)
    next(drd, None)
    for row in drd:
        print(row[0])

        Store.objects.create(
            name = row[0],
            address = row[1],
            business_day = row[2],
            opening_hour = row[3],
            contact = row[4]
        )