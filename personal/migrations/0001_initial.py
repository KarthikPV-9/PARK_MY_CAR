# Generated by Django 3.2 on 2021-05-01 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=10, null=True)),
                ('slot_id', models.CharField(max_length=10)),
                ('want_to_book_the_slot', models.BooleanField(default=False)),
                ('vehicle_id', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='parking_slot',
            fields=[
                ('parking_vehicle', models.CharField(max_length=5, null=True)),
                ('booked_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('slot_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('is_occupied', models.BooleanField(default=False)),
                ('available_increment', models.PositiveSmallIntegerField(default=60)),
                ('vehicle_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('company', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('parked', models.BooleanField(default=False)),
                ('parked_slot_id', models.CharField(max_length=10, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personal.vehicle')),
                ('geared', models.BooleanField(default=True)),
            ],
            bases=('personal.vehicle',),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personal.vehicle')),
                ('auto_gear', models.BooleanField(default=False)),
                ('auto_trans', models.BooleanField(default=False)),
            ],
            bases=('personal.vehicle',),
        ),
    ]