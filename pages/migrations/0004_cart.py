# Generated by Django 5.1 on 2024-10-05 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0003_alter_categories_cat_image_alter_product_pr_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("cart_id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                (
                    "pr_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.product"
                    ),
                ),
                (
                    "user_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
