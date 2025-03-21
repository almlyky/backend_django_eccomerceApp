# Generated by Django 4.2 on 2025-02-16 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Adds",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images/adds/%y/%m/%d")),
                ("url", models.URLField()),
                ("date_adds", models.DateField(auto_now_add=True)),
                ("expired_adds", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Categories",
            fields=[
                ("cat_id", models.AutoField(primary_key=True, serialize=False)),
                ("cat_name", models.CharField(max_length=50)),
                ("cat_name_en", models.CharField(max_length=50)),
                (
                    "cat_image",
                    models.ImageField(upload_to="images/categories/%y/%m/%d"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coupon",
            fields=[
                ("co_id", models.AutoField(primary_key=True, serialize=False)),
                ("co_name", models.CharField(max_length=50, unique=True)),
                ("co_count", models.IntegerField()),
                ("co_discount", models.IntegerField()),
                ("co_expiredate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("cash", "نقدا"), ("transfer", "ارسال حوالة")],
                        default="cash",
                        max_length=50,
                    ),
                ),
                (
                    "order_type",
                    models.CharField(
                        choices=[("delivery", "Delivery"), ("recive", "Recive")],
                        default="delivery",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("address", models.CharField(max_length=100)),
                ("total_order", models.IntegerField()),
                ("order_code", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("pr_id", models.AutoField(primary_key=True, serialize=False)),
                ("pr_name", models.CharField(max_length=50)),
                ("pr_name_en", models.CharField(max_length=50)),
                ("pr_image", models.ImageField(upload_to="images/product/%y/%m/%d")),
                ("pr_cost", models.IntegerField()),
                ("pr_cost_new", models.IntegerField(default=0)),
                ("pr_detail", models.CharField(max_length=150)),
                ("pr_detail_en", models.CharField(max_length=150)),
                ("pr_discoutn", models.IntegerField(default=0)),
                (
                    "cat_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="pages.categories",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("discount_percentage", models.IntegerField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                ("fav_no", models.AutoField(primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("cart_id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                ("order", models.IntegerField(default=0)),
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
