
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
