# Generated by Django 4.0.4 on 2022-05-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='describtion',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
