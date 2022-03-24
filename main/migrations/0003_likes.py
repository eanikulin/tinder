# Generated by Django 4.0.2 on 2022-03-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_options_alter_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator_like', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
                'ordering': ('-pk',),
            },
        ),
    ]