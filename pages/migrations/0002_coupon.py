# Generated by Django 5.1 on 2024-11-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
            fields=[
                ("co_id", models.AutoField(primary_key=True, serialize=False)),
                ("co_name", models.CharField(max_length=50, unique=True)),
                ("co_count", models.IntegerField()),
                ("co_discount", models.IntegerField()),
                ("co_expiredate", models.DateTimeField()),
            ],
        ),
    ]
