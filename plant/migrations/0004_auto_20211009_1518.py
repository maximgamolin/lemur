# Generated by Django 3.2.8 on 2021-10-09 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0003_auto_20211009_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workpiece',
            old_name='new_features',
            new_name='features',
        ),
        migrations.RemoveField(
            model_name='workpiece',
            name='aggregation',
        ),
        migrations.DeleteModel(
            name='DataSamplingUnionParent',
        ),
    ]
