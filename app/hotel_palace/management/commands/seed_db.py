from django.core.management.base import BaseCommand
from ...factory import factories as db_factory

class Command(BaseCommand):
    help = 'Populates the database with test data.'

    def add_arguments(self, parser):
        parser.add_argument('data_quant', nargs='?', type=int, default=15, help='Number of records to create.')

    def handle(self, *args, **options):
        data_quant = options['data_quant']
        db_factory.CategoryFactory.create_batch(data_quant)
        db_factory.RoomFactory.create_batch(data_quant)
        db_factory.CustomerFactory.create_batch(data_quant)
        db_factory.ProductFactory.create_batch(data_quant)
        db_factory.ReservationFactory.create_batch(data_quant)
        db_factory.AccommodationFactory.create_batch(data_quant)
        db_factory.ConsumeFactory.create_batch(data_quant)

        self.stdout.write(self.style.SUCCESS(f'{data_quant} records successfully seeded.'))
