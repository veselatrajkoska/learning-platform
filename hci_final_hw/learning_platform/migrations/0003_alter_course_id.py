# Generated by Django 4.1 on 2022-08-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_platform', '0002_alter_course_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
