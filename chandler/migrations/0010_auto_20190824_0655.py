# Generated by Django 2.2.4 on 2019-08-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chandler', '0009_auto_20190824_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistroy',
            name='checksum',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistroy',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistroy',
            name='item_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistroy',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistroy',
            name='txnid',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
