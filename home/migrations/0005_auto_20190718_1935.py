# Generated by Django 2.2.3 on 2019-07-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190718_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='body',
            field=models.CharField(max_length=2000),
        ),
    ]