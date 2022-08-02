# Generated by Django 4.0.5 on 2022-08-02 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
        ('teacher', '0010_alter_quesmodel_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.createclass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.student')),
            ],
        ),
    ]
