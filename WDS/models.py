from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class Customer(models.Model):
    ssn_number = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    marital_status = models.CharField(max_length=1)
    type = models.CharField(max_length=1)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'customer'


class Driver(models.Model):
    liscense_num = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    vehicle_vin = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehicle_vin')

    class Meta:
        managed = False
        db_table = 'driver'


class HousePremium(models.Model):
    premium_id = models.IntegerField(primary_key=True)
    afn = models.IntegerField()
    hss = models.IntegerField()
    swimming_pool = models.CharField(max_length=1, blank=True, null=True)
    basement = models.IntegerField()
    premium_amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'house_premium'


class Houses(models.Model):
    house_id = models.BigIntegerField(primary_key=True)
    purchase_date = models.DateTimeField()
    purchase_value = models.BigIntegerField()
    area = models.BigIntegerField()
    house_type = models.CharField(max_length=1)
    policy = models.ForeignKey('Policy', models.DO_NOTHING, blank=True, null=True)
    premium = models.ForeignKey(HousePremium, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'houses'


class Invoice(models.Model):
    invoice_id = models.BigIntegerField(primary_key=True)
    due_date = models.DateTimeField()
    amount = models.IntegerField()
    ssn_number = models.ForeignKey(Customer, models.DO_NOTHING, db_column='ssn_number')
    policy = models.ForeignKey('Policy', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'invoice'


class Payment(models.Model):
    reciept_id = models.BigIntegerField(primary_key=True)
    payment_date = models.DateTimeField()
    method = models.CharField(max_length=2)
    installment_amount = models.IntegerField()
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Policy(models.Model):
    policy_id = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    insurance_status = models.CharField(max_length=1)
    type = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'policy'


class Vehicle(models.Model):
    vin = models.CharField(primary_key=True, max_length=17)
    vehicle_make = models.CharField(max_length=10)
    vehicle_model = models.CharField(max_length=10)
    vehicle_status = models.CharField(max_length=1)
    vehicle_year = models.SmallIntegerField()
    policy = models.ForeignKey(Policy, models.DO_NOTHING, blank=True, null=True)
    premium_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehicle'