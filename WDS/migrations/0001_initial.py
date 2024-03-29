# Generated by Django 3.0.5 on 2020-04-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ssn_number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('marital_status', models.CharField(max_length=1)),
                ('type', models.CharField(max_length=1)),
                ('mobile_number', models.BigIntegerField(blank=True, null=True)),
                ('email_id', models.CharField(blank=True, max_length=30, null=True)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('liscense_num', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'driver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HousePremium',
            fields=[
                ('premium_id', models.IntegerField(primary_key=True, serialize=False)),
                ('afn', models.IntegerField()),
                ('hss', models.IntegerField()),
                ('swimming_pool', models.CharField(blank=True, max_length=1, null=True)),
                ('basement', models.IntegerField()),
                ('premium_amount', models.BigIntegerField()),
            ],
            options={
                'db_table': 'house_premium',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('house_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateTimeField()),
                ('purchase_value', models.BigIntegerField()),
                ('area', models.BigIntegerField()),
                ('house_type', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'houses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('due_date', models.DateTimeField()),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'invoice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('reciept_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField()),
                ('method', models.CharField(max_length=2)),
                ('installment_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('policy_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('insurance_status', models.CharField(max_length=1)),
                ('type', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'policy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vin', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('vehicle_make', models.CharField(max_length=10)),
                ('vehicle_model', models.CharField(max_length=10)),
                ('vehicle_status', models.CharField(max_length=1)),
                ('vehicle_year', models.SmallIntegerField()),
                ('premium_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'vehicle',
                'managed': False,
            },
        ),
    ]
