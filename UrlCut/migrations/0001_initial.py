# Generated by Django 3.0.7 on 2020-06-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.TextField()),
                ('short_url', models.CharField(db_index=True, max_length=50, unique=True)),
                ('usage_count', models.IntegerField(default=0, null=True)),
                ('usage_count_limit', models.IntegerField(default=-1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
