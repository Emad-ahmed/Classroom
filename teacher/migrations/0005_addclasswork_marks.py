# Generated by Django 4.0.5 on 2022-07-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_addclasswork'),
    ]

    operations = [
        migrations.AddField(
            model_name='addclasswork',
            name='marks',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
