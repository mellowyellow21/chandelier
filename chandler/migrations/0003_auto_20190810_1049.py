# Generated by Django 2.2.4 on 2019-08-10 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chandler', '0002_auto_20190810_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chandler.Product'),
            preserve_default=False,
        ),
    ]
