# Generated by Django 5.0.2 on 2025-06-27 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gates", "0003_alter_gate_image_gateimage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="GateImage",
        ),
    ]
