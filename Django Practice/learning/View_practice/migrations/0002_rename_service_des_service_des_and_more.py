# Generated by Django 4.2.4 on 2023-09-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('View_practice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_des',
            new_name='des',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_Title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='title',
        ),
    ]
