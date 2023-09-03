
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
