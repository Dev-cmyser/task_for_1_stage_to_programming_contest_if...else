# Generated by Django 4.1.6 on 2023-02-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "animal_api",
            "0005_animal_alter_location_options_alter_user_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="chipping_date_time",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="chipping_date_time"
            ),
        ),
    ]
