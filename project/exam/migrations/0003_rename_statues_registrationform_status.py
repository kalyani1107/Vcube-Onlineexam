# Generated by Django 4.1.3 on 2023-02-02 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_registrationform_statues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='statues',
            new_name='status',
        ),
    ]
