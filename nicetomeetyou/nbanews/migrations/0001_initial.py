# Generated by Django 2.1.1 on 2018-09-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NbaNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.PositiveIntegerField(unique=True)),
                ('reporter', models.CharField(blank=True, default='', max_length=100)),
                ('post_title', models.CharField(blank=True, default='', max_length=300)),
                ('image_url', models.CharField(blank=True, default='', max_length=1024)),
                ('post_url', models.CharField(blank=True, default='', max_length=1024)),
                ('timestamp', models.DateTimeField()),
                ('post_content', models.TextField(blank=True, default='')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
