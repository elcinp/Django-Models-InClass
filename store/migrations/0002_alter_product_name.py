# Generated by Django 3.2.8 on 2021-10-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default='No Name', max_length=50, null=True),
        ),
    ]
