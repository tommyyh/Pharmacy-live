# Generated by Django 3.2.6 on 2021-09-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_auto_20210925_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='nhs_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='nhs_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
