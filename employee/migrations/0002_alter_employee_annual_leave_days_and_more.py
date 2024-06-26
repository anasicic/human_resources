# Generated by Django 4.2.11 on 2024-06-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="annual_leave_days",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="free_days",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="paid_leave_days",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
