# Generated by Django 3.2.4 on 2024-07-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_template_customtemplates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='CV',
            field=models.FileField(blank=True, upload_to='cv/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='transcript',
            field=models.FileField(blank=True, upload_to='transcript/'),
        ),
    ]