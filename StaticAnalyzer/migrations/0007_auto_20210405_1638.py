# Generated by Django 3.1.7 on 2021-04-05 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StaticAnalyzer', '0006_auto_20210405_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticanalyzerandroid',
            old_name='FILE_ANALYSIS',
            new_name='EMAILS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='DOMAINS',
        ),
        migrations.RemoveField(
            model_name='staticanalyzerandroid',
            name='FIREBASE_URLS',
        ),
    ]
