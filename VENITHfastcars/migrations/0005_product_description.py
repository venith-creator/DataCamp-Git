# Generated by Django 5.2 on 2025-05-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VENITHfastcars', '0004_remove_contactmessage_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
