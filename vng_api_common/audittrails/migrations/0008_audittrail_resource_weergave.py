# Generated by Django 2.2.2 on 2019-06-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audittrails', '0007_auto_20190522_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='audittrail',
            name='resource_weergave',
            field=models.CharField(default='', help_text='Vriendelijke identificatie van het object', max_length=200),
            preserve_default=False,
        ),
    ]
