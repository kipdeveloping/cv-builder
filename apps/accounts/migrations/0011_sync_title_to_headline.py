from django.db import migrations


def sync_title_to_headline(apps, schema_editor):
    pass


def reverse_sync_title_to_headline(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_userprofile_title'),
    ]

    operations = [
        migrations.RunPython(sync_title_to_headline, reverse_sync_title_to_headline),
    ]
