# Generated by Django 5.0.2 on 2024-02-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
    ]
