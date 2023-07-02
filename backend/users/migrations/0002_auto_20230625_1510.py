# Generated by Django 4.1.2 on 2023-06-25 15:10
from django.contrib.auth.models import Group
from django.db import migrations


def create_groups(apps, schema_editor):
    teachers_group = Group(name="Teachers")
    students_group = Group(name="Students")

    teachers_group.save()
    students_group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]