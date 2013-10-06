# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('myapp', '0001_initial')]

    operations = [
        migrations.AlterUniqueTogether(
            name = 'item',
            unique_together = set(['text', 'list']),
        ),
    ]
