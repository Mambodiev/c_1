# Generated by Django 3.0 on 2021-06-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttranslation',
            name='secondary_categories',
        ),
        migrations.AddField(
            model_name='product',
            name='secondary_categories',
            field=models.ManyToManyField(blank=True, to='cart.Category'),
        ),
    ]