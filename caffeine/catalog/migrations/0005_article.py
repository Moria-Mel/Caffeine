# Generated by Django 3.2.5 on 2021-12-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('summary', models.TextField()),
                ('links', models.TextField(null=True)),
            ],
        ),
    ]
