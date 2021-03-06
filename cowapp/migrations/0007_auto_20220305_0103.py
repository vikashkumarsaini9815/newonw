# Generated by Django 3.2.10 on 2022-03-04 19:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0006_alter_user_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='updated',
        ),
        migrations.AddField(
            model_name='amount_info',
            name='join_dates',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amount_info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='cowapp.user'),
        ),
    ]
