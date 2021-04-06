# Generated by Django 3.1.5 on 2021-03-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210311_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefile',
            name='date',
            field=models.DateField(auto_now_add=True, default=-2020),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='linkto',
            field=models.CharField(choices=[('slide', 'स्\u200dलाईड'), ('logo', 'लोगो'), ('newspaper', 'सामाचार पत्र')], max_length=100),
        ),
    ]