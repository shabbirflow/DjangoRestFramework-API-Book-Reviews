# Generated by Django 5.0.1 on 2024-01-13 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booksapp", "0004_rename_apilogsmodel_apilogsmodel2"),
    ]

    operations = [
        migrations.DeleteModel(
            name="APILogsModel2",
        ),
    ]
