from django.core.management import BaseCommand
from tqdm import tqdm

try:
    from wagtail.core.models import Page
except ImportError:  # pragma: no cover; fallback for Wagtail <2.0
    from wagtail.wagtailcore.models import Page

from wagtailinventory.helpers import (
    create_page_inventory, delete_page_inventory
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        delete_page_inventory()

        pages = Page.objects.all()

        if options.get('verbosity'):  # pragma: no cover
            pages = tqdm(pages)

        for page in pages:
            create_page_inventory(page)
