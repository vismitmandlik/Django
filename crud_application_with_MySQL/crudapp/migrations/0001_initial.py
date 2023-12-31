# Generated by Django 4.1 on 2022-08-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("uname", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("upassword", models.CharField(max_length=100)),
            ],
            options={"db_table": "users",},
        ),
    ]
