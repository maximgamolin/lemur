# Generated by Django 3.2.8 on 2021-10-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpiece',
            name='aggregation',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workpiece',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='workpiece',
            name='limits',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workpiece',
            name='new_features',
            field=models.JSONField(blank=True, null=True),
        ),
    ]