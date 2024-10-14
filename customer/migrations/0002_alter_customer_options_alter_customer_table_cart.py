# Generated by Django 5.1 on 2024-09-24 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('restaurant', '0004_foods_food_category_alter_foods_store'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-id'], 'verbose_name': 'customer', 'verbose_name_plural': 'customer'},
        ),
        migrations.AlterModelTable(
            name='customer',
            table='Customer_customer',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.foods')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.store')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'db_table': 'customer_cart',
                'ordering': ['-id'],
            },
        ),
    ]
