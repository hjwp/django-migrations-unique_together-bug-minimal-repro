# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name = 'List',
            options = {},
            fields = [('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True),)],
            bases = (models.Model,),
        ),
        migrations.CreateModel(
            name = 'Item',
            options = {},
            fields = [('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True),), ('list', models.ForeignKey(to_field='id', to='myapp.List'),), ('text', models.TextField(),)],
            bases = (models.Model,),
        ),
    ]
