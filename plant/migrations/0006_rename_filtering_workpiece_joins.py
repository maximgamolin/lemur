# Generated by Django 3.2.8 on 2021-10-09 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0005_auto_20211009_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workpiece',
            old_name='filtering',
            new_name='joins',
        ),
    ]
