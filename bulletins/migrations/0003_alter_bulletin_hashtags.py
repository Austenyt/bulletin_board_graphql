# Generated by Django 5.1.3 on 2024-12-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bulletins", "0002_bulletin_hashtags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bulletin",
            name="hashtags",
            field=models.JSONField(
                blank=True, default=list, help_text="Введите хэштеги через запятую"
            ),
        ),
    ]
