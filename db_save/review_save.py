import os, sys, csv, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hice.settings")
django.setup()

from reviews.models import Review

CSV_PATH = '/home/taehyun/Wecode/11-Hipce-backend/crawling/review_crawling.csv'

with open(CSV_PATH) as f:
    drd = csv.reader(f)
    next(drd, None)

    for row in drd:
        Review.objects.create(
            
        )