# Generated by Django 2.1.2 on 2018-11-03 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights3.Airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flights3.Airport'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights3.Flight'),
        ),
    ]
