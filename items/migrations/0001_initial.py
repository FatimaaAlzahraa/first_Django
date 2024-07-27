# Generated by Django 5.0.7 on 2024-07-19 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ApparelSize",
            fields=[
                ("size_id", models.AutoField(primary_key=True, serialize=False)),
                ("size_code", models.CharField(max_length=100)),
                ("other_data", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ProductColor",
            fields=[
                ("color_id", models.AutoField(primary_key=True, serialize=False)),
                ("color_code", models.CharField(max_length=100)),
                ("color_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_name", models.CharField(max_length=100)),
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items.apparelsize",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items.productcolor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategories",
            fields=[
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=100)),
                (
                    "category_id_parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items.productcategories",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="items.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Categories",
            fields=[
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=100)),
                (
                    "product_categories",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items.productcategories",
                    ),
                ),
            ],
        ),
    ]
