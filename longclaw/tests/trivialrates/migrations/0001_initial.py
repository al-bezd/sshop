# Generated by Django 2.1.7 on 2019-03-23 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0003_auto_20190322_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrivialShippingRateProcessor',
            fields=[
                ('shippingrateprocessor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shipping.ShippingRateProcessor')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('shipping.shippingrateprocessor',),
        ),
    ]
