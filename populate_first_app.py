import os
import random
from first_app.models import AccessRecord, Topic, WebPage
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        top = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        web = WebPage.objects.get_or_create(
            topic=top,
            url=fake_url,
            name=fake_name,
        )[0]

        acc_rec = AccessRecord.objects.get_or_create(
            name=web,
            date=fake_date,
        )[0]


# TODO find out why is not working
if __name__ == '__main__':
    print('populating script!')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tangle.settings')

    import django

    django.setup()

    populate(20)
    print('populating complete!')
