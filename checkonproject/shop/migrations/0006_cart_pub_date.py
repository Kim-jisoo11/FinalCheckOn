# Generated by Django 3.1.2 on 2020-10-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20201022_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
