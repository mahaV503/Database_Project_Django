from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class Customer(models.Model):
    types=('H','Home Insurance'),('A','Auto Insurance')
    g_types=('M','Male'),('F','Female')
    m_status=('S','Single'),('M','Married'),('W','Widowed')
    state_choices = (('AL', 'Alabama'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'))

    ssn_number = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1,choices=g_types)
    marital_status = models.CharField(max_length=1)
    type = models.CharField(max_length=1,choices=types)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15,choices=state_choices)
    zip_code = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return str(self.first_name+''+self.last_name)


class Driver(models.Model):
    liscense_num = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    vehicle_vin = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehicle_vin')

    class Meta:
        managed = False
        db_table = 'driver'
    def __str__(self):
        return str(self.liscense_num)


class HousePremium(models.Model):
    afn_types=(1,'Has Auto Fire Notification'),(0,"Don't have an AFN")
    hss_types=(1,'Has Home Security System'),(0,"Don't have an HSS")
    swimmingpool_types=('U','Underground'),('O','Overground'),('I','Indoor'),('M','Multiple')
    basement_types=(1,'Has a basement'),(0,"Don't have a basement")
    
    premium_id = models.IntegerField(primary_key=True)
    afn = models.IntegerField(choices=afn_types)
    hss = models.IntegerField(choices=hss_types)
    swimming_pool = models.CharField(max_length=1, blank=True, null=True,choices=swimmingpool_types)
    basement = models.IntegerField(choices=basement_types)
    premium_amount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'house_premium'
    def __str__(self):
        return str(self.premium_id)


class Houses(models.Model):
    house_type=('S','Signle Family'),('M','Multi Family'),('C','Condominium'),('T','Town House')
    house_id = models.BigIntegerField(primary_key=True)
    purchase_date = models.DateTimeField()
    purchase_value = models.BigIntegerField()
    area = models.BigIntegerField()
    house_type = models.CharField(max_length=1,choices=house_type)
    policy = models.ForeignKey('Policy', models.DO_NOTHING, blank=True, null=True)
    premium = models.ForeignKey(HousePremium, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'houses'
    def __str__(self):
        return str(self.house_id)


class Invoice(models.Model):
    invoice_id = models.BigIntegerField(primary_key=True)
    due_date = models.DateTimeField()
    amount = models.IntegerField()
    ssn_number = models.ForeignKey(Customer, models.DO_NOTHING, db_column='ssn_number')
    policy = models.ForeignKey('Policy', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'invoice'
    def __str__(self):
        return str(self.invoice_id)


class Payment(models.Model):
    payment_types=('PP','PayPal'),('Cr','Credit'),('De','Debit'),('Ch','Check')
    reciept_id = models.BigIntegerField(primary_key=True)
    payment_date = models.DateTimeField()
    method = models.CharField(max_length=2,choices=payment_types)
    installment_amount = models.IntegerField()
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
    def __str__(self):
        return str(self.reciept_id)


class Policy(models.Model):
    type_types=('H','Home Insurance'),('A','Auto Insurance')
    ins_sta_types=('C','Current'),('P','Payment')
    policy_id = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    insurance_status = models.CharField(max_length=1,choices=ins_sta_types)
    type = models.CharField(max_length=1,choices=type_types)

    class Meta:
        managed = False
        db_table = 'policy'
    def __str__(self):
        return str(self.policy_id)


class Vehicle(models.Model):
    vehicle_sta_types=('L','Leased'),('F','Financed'),('O','Owned')
    vin = models.CharField(primary_key=True, max_length=17)
    vehicle_make = models.CharField(max_length=10)
    vehicle_model = models.CharField(max_length=10)
    vehicle_status = models.CharField(max_length=1,choices=vehicle_sta_types)
    vehicle_year = models.SmallIntegerField()
    policy = models.ForeignKey(Policy, models.DO_NOTHING, blank=True, null=True)
    premium_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehicle'
    def __str__(self):
        return str(self.vin)