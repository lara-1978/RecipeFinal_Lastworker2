# Generated by Django 5.1.5 on 2025-01-23 10:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_category_recipecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
