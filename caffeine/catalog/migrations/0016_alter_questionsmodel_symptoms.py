# Generated by Django 3.2.5 on 2022-01-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20220124_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='symptoms',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
