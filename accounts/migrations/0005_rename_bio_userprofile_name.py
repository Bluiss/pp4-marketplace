from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts',
         '0004_remove_userprofile_email_userprofile_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='bio',
            new_name='name',
        ),
    ]
