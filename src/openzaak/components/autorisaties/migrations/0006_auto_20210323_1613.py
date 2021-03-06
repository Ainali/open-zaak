# SPDX-License-Identifier: EUPL-1.2
# Copyright (C) 2021 Dimpact
# Generated by Django 2.2.17 on 2021-03-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autorisaties", "0005_fill_nlx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autorisatiespec",
            name="component",
            field=models.CharField(
                choices=[
                    ("ac", "Autorisaties API"),
                    ("nrc", "Notificaties API"),
                    ("zrc", "Zaken API"),
                    ("ztc", "Catalogi API"),
                    ("drc", "Documenten API"),
                    ("brc", "Besluiten API"),
                ],
                help_text="Component waarop autorisatie van toepassing is.",
                max_length=50,
                verbose_name="component",
            ),
        ),
    ]
