# Generated by Django 5.0.4 on 2024-04-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_alter_quote_author_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author_fullname',
            field=models.CharField(max_length=100),
        ),
    ]
