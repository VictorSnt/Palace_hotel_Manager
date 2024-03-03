from django.db import models
from .enums.brazilian_states import BrazilianStates
from .enums.marital_status import MaritalStatus
from .enums.room_status import RoomStatus
from .enums.gender import Gender
import uuid


class RoomCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, unique=True, null=False)
    one_guest_price = models.DecimalField(max_digits=10, decimal_places=2)
    two_guest_price = models.DecimalField(max_digits=10, decimal_places=2)
    three_guest_price = models.DecimalField(max_digits=10, decimal_places=2)
    four_guest_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (
            f'{self.description}: {self.one_guest_price}|'
            f'{self.two_guest_price}|{self.three_guest_price}|'
            f'{self.four_guest_price}'
    )
class Product(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=80, null=False)
    price = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description}| preço: {self.price}"

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    rg = models.CharField(max_length=9, blank=True, null=True)
    gender = models.CharField(
        max_length=4, choices=[(g.value, g.name) for g in Gender],
        blank=True, null=True
    )
    marital_status = models.CharField(
        max_length=15, choices=[(ms.value, ms.name) for ms in MaritalStatus],
        blank=True, null=True
    )
    partner = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=25, blank=True, null=True)
    occupation_company_name = models.CharField(
        max_length=25, blank=True, null=True
    )
    zip_code = models.CharField(max_length=25, blank=True, null=True)
    address_street = models.CharField(max_length=50, blank=True, null=True)
    address_number = models.CharField(max_length=6, blank=True, null=True)
    address_ref = models.CharField(max_length=25, blank=True, null=True)
    address_district = models.CharField(max_length=50, blank=True, null=True)
    address_city = models.CharField(max_length=20, blank=True, null=True)
    address_uf = models.CharField(
        max_length=2, choices=[(s.value, s.name) for s in BrazilianStates],
        blank=True, null=True
    )
    phone = models.CharField(max_length=15)
    cellphone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} - CPF: {self.cpf or "Sem cpf registrado"}'

class Room(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=3, null=False, unique=True)
    status = models.CharField(
        max_length=10, 
        choices=[(s.value, s.name) for s in RoomStatus],
        default='FREE'
    )
    category = models.ForeignKey(RoomCategory, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.room_number)

    
class RoomReservation(models.Model):
    GUEST_QUANT = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='reservations')
    costumer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    guest_quant = models.CharField(max_length=10, choices=GUEST_QUANT, default='1')
    open = models.BooleanField(default=True)
    days_quant = models.IntegerField()
    checkin_date = models.DateField(null=False)
    checkout_date = models.DateField(null=False)
    checkin_time = models.TimeField(null=True)
    checkout_time = models.TimeField(null=True)
    hosting_price = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    total_hosting_price = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    total_bill = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Reservation {self.checkout_date} for Room {self.room_id}'

class ProductConsume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_reservation_id = models.ForeignKey(RoomReservation, on_delete=models.PROTECT, related_name='consumes')
    room_id = models.ForeignKey(Room, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    qtproduct = models.IntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product {self.product_id} consumed in Room {self.room_id}'

class HotelReservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='reservation')
    checkin_date = models.DateField(null=False)
    customer_name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Check-in: {self.checkin_date}'
    