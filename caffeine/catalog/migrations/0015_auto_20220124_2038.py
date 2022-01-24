# Generated by Django 3.2.5 on 2022-01-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20220124_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsmodel',
            name='addiction1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='addiction2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='addiction3',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='energy_drinks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='grain_coffee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='instant_coffee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='pills',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='symptoms',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='tea',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='job',
            field=models.CharField(max_length=2),
        ),
    ]
