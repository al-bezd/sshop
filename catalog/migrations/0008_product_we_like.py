# Generated by Django 3.1.4 on 2020-12-07 16:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20201207_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='we_like',
            field=wagtail.core.fields.StreamField([('WeLike', wagtail.core.blocks.StructBlock([]))], blank=True),
        ),
    ]
