# Generated by Django 2.2.2 on 2019-07-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190728_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='designation',
            field=models.CharField(blank=True, default='Core Member', max_length=100),
        ),
    ]
