# Generated by Django 5.1.3 on 2024-12-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bulletins", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bulletin",
            name="hashtags",
            field=models.JSONField(default=list),
        ),
    ]
