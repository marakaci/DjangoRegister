# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20170618_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Class',
            new_name='Grade',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='class_number',
            new_name='grade_number',
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Subject'),
        ),
        migrations.AddField(
            model_name='gradesubject',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Grade'),
        ),
        migrations.AddField(
            model_name='gradesubject',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Subject'),
        ),
        migrations.AddField(
            model_name='gradesubject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Teacher'),
        ),
    ]
