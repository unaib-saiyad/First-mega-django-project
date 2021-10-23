# Generated by Django 3.2.6 on 2021-10-21 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('subject', models.CharField(default='', max_length=100)),
                ('tags', models.CharField(default='', max_length=50)),
                ('body', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='forum/')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
