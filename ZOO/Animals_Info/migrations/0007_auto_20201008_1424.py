# Generated by Django 3.0.6 on 2020-10-08 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Animals_Info', '0006_auto_20201008_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal_place',
            old_name='nickname',
            new_name='nickname_3',
        ),
        migrations.AddField(
            model_name='animal_place',
            name='nickname_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nickname_1', to='Animals_Info.Animal', verbose_name='Выберите животное #1'),
        ),
        migrations.AddField(
            model_name='animal_place',
            name='nickname_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nickname_2', to='Animals_Info.Animal', verbose_name='Выберите животное #2'),
        ),
    ]