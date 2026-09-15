from django.db import migrations


def populate_sector_fk(apps, schema_editor):
    UserProfile = apps.get_model('accounts', 'UserProfile')
    SectorTag = apps.get_model('accounts', 'SectorTag')
    
    try:
        default_sector = SectorTag.objects.get(slug='tecnologia')
    except SectorTag.DoesNotExist:
        return
    
    UserProfile.objects.filter(sector__isnull=True).update(sector=default_sector)


def reverse_populate_sector_fk(apps, schema_editor):
    UserProfile = apps.get_model('accounts', 'UserProfile')
    UserProfile.objects.filter(sector__isnull=False).update(sector=None)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_userprofile_sector_name'),
    ]

    operations = [
        migrations.RunPython(populate_sector_fk, reverse_populate_sector_fk),
    ]
