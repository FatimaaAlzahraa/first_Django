# Generated by Django 5.0.7 on 2024-07-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productcategories",
            name="category_id_parent",
        ),
    ]
