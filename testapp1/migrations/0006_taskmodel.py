# Generated by Django 3.2 on 2021-06-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0005_alter_login_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
