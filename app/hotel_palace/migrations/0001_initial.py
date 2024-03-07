# Generated by Django 5.0.2 on 2024-03-07 23:31

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255, unique=True)),
                ('one_guest_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('two_guest_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('three_guest_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('four_guest_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('rg', models.CharField(blank=True, max_length=9, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Masc', 'MALE'), ('Fem', 'FEMALE')], max_length=4, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Solteiro(a)', 'SINGLE'), ('Casado(a)', 'MARRIED'), ('Divorciado(a)', 'DIVORCED'), ('Viúvo(a)', 'WIDOWED')], max_length=15, null=True)),
                ('partner', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=25, null=True)),
                ('occupation_company_name', models.CharField(blank=True, max_length=25, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=25, null=True)),
                ('address_street', models.CharField(blank=True, max_length=50, null=True)),
                ('address_number', models.CharField(blank=True, max_length=6, null=True)),
                ('address_ref', models.CharField(blank=True, max_length=25, null=True)),
                ('address_district', models.CharField(blank=True, max_length=50, null=True)),
                ('address_city', models.CharField(blank=True, max_length=20, null=True)),
                ('address_uf', models.CharField(blank=True, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO_FEDERAL'), ('ES', 'ESPIRITO_SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'), ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'), ('MG', 'MINAS_GERAIS'), ('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'), ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'), ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'), ('SC', 'SANTA_CATARINA'), ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'), ('TO', 'TOCANTINS')], max_length=2, null=True)),
                ('phone', models.CharField(max_length=21)),
                ('cellphone', models.CharField(blank=True, max_length=21, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('guest_quant', models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE'), ('4', 'FOUR')], default='1', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('days_quant', models.IntegerField()),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('checkin_time', models.TimeField(null=True)),
                ('checkout_time', models.TimeField(null=True)),
                ('hosting_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_hosting_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_bill', models.DecimalField(decimal_places=2, max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_palace.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=3, unique=True)),
                ('status', models.CharField(choices=[('Livre', 'FREE'), ('Ocupado', 'OCCUPIED'), ('Sujo', 'DIRTY'), ('Manutenção', 'MAINTENANCE')], default='FREE', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_palace.category')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checkin_date', models.DateField()),
                ('customer_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to='hotel_palace.room')),
            ],
        ),
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room_reservation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consumes', to='hotel_palace.accommodation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_palace.product')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_palace.room')),
            ],
        ),
        migrations.AddField(
            model_name='accommodation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accommodations', to='hotel_palace.room'),
        ),
    ]
