# Generated by Django 5.2 on 2025-06-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_member_phone_number_alter_member_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
