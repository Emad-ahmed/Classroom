# Generated by Django 4.0.5 on 2022-07-11 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_quesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='myclass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.createclass'),
        ),
    ]
