# Generated by Django 4.1.3 on 2023-02-03 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_remove_registrationform_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='password',
        ),
    ]
