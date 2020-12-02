# Generated by Django 3.1.3 on 2020-11-29 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20201116_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
            ],
            options={
                'verbose_name': 'Booked Day',
                'verbose_name_plural': 'Booked Days',
            },
        ),
    ]
