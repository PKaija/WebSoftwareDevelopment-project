# Generated by Django 3.0.3 on 2020-02-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20200207_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]