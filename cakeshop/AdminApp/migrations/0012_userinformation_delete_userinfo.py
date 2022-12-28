# Generated by Django 4.1.2 on 2022-11-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'UserInformation',
            },
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
