# Generated by Django 3.0.6 on 2020-10-08 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Animals_Info', '0003_auto_20201008_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal_place',
            name='nickname',
        ),
        migrations.AddField(
            model_name='animal_place',
            name='nickname1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Animals_Info.Animal', verbose_name='Выберите животное'),
        ),
    ]
