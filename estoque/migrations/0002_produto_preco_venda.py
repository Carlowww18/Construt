# Generated by Django 5.1.3 on 2024-11-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estoque", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="preco_venda",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
