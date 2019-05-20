# Generated by Django 2.0.13 on 2019-05-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audittrails', '0003_auto_20190517_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='audittrail',
            name='gebruikers_id',
            field=models.CharField(blank=True, help_text='Unieke identificatie van de gebruiker die binnen de organisatie herleid kan worden naar een persoon', max_length=255),
        ),
        migrations.AddField(
            model_name='audittrail',
            name='gebruikers_weergave',
            field=models.CharField(blank=True, help_text='Vriendelijke naam van de gebruiker', max_length=255),
        ),
    ]