# Generated by Django 2.2.1 on 2019-05-09 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.CharField(max_length=9999)),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.IntegerField()),
                ('ssn', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('Zip', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('kingdom', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='userlogin',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
        migrations.AddField(
            model_name='profile',
            name='zip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Zip'),
        ),
    ]