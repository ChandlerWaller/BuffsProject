# Generated by Django 4.2 on 2024-04-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buffs_app', '0003_alter_shift_date_alter_shift_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='position',
            field=models.CharField(choices=[('1st Bar', 'First Person Cut in Bar'), ('1st Dinning', 'First Person Cut in Dinning'), ('Late Stay Bar', 'Second Person Cut in Bar'), ('Late Stay Dinning', 'Second Person Cut in Dinning'), ('Carpet Closer', 'Closer for Dinning'), ('Bar Closer', 'Closer for Bar')], default='Position of Shift', max_length=200),
        ),
        migrations.AlterField(
            model_name='shift',
            name='time',
            field=models.TimeField(),
        ),
    ]
