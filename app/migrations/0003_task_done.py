# Generated by Django 4.0.6 on 2022-08-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], default='status', max_length=5),
        ),
    ]
