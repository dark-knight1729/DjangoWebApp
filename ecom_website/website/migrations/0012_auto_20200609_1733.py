# Generated by Django 3.0.6 on 2020-06-09 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0011_auto_20200609_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetail',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Service',
                                    verbose_name='Service'),
        ),
    ]
