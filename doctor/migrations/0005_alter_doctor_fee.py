# Generated by Django 4.2.7 on 2024-05-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_doctor_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='fee',
            field=models.IntegerField(),
        ),
    ]
