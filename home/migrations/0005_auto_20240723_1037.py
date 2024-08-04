# Generated by Django 3.2.4 on 2024-07-23 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20240717_1404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentData',
            new_name='Application',
        ),
        migrations.RenameField(
            model_name='academics',
            old_name='student',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='files',
            old_name='student',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='student',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='student',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='qualities',
            old_name='student',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='student',
            new_name='application',
        ),
        migrations.AlterModelTable(
            name='application',
            table='Application',
        ),
    ]