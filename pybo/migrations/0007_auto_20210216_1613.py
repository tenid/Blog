# Generated by Django 3.1.6 on 2021-02-16 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_answer_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='question_key',
        ),
    ]