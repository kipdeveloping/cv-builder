from django.core.management.base import BaseCommand
from django.db.models import Q
from apps.accounts.models import UserProfile, SectorTag


class Command(BaseCommand):
    help = 'Migrate existing sector_name text values to sector FK on UserProfile'

    def handle(self, *args, **options):
        profiles = UserProfile.objects.filter(
            sector_name__isnull=False
        ).exclude(
            sector_name=''
        ).select_related('sector')

        updated = 0
        skipped = 0
        not_found = 0
        errors = []

        for profile in profiles:
            if profile.sector:
                skipped += 1
                continue

            sector_name = profile.sector_name.strip()
            sector = SectorTag.objects.filter(
                Q(name_es__iexact=sector_name) |
                Q(name_en__iexact=sector_name) |
                Q(slug__iexact=sector_name)
            ).first()

            if sector:
                profile.sector = sector
                profile.save(update_fields=['sector'])
                updated += 1
                self.stdout.write(
                    f'  Migrated profile {profile.user.email}: '
                    f'"{sector_name}" -> "{sector.name_es}"'
                )
            else:
                not_found += 1
                errors.append(f'Profile {profile.user.email}: sector "{sector_name}" not found in dictionary')

        self.stdout.write(self.style.SUCCESS(
            f'\nMigration complete: {updated} updated, {skipped} skipped (already set), {not_found} not found'
        ))

        if errors:
            self.stdout.write(self.style.WARNING('\nProfiles with unknown sectors:'))
            for err in errors:
                self.stdout.write(f'  - {err}')
