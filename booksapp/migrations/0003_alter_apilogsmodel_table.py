# Generated by Django 5.0.1 on 2024-01-13 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booksapp", "0002_apilogsmodel"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="apilogsmodel",
            table="drf_api_logs2",
        ),
    ]
