# Generated by Django 4.2.11 on 2024-06-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0002_alter_employee_annual_leave_days_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="contract_type",
            field=models.CharField(
                choices=[("permanent", "Permanent"), ("fixed-term", "Fixed-term")],
                default="temporary",
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="employee",
            name="department",
            field=models.CharField(
                choices=[
                    ("hr", "Human Resources"),
                    ("it", "Information Technology"),
                    ("sales", "Sales"),
                    ("finance", "Finance"),
                    ("marketing", "Marketing"),
                ],
                default="temporary",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]