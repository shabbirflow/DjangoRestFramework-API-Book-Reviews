# Generated by Django 5.0.1 on 2024-01-13 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booksapp", "0003_alter_apilogsmodel_table"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="APILogsModel",
            new_name="APILogsModel2",
        ),
    ]
