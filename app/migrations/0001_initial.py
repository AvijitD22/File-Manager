# Generated by Django 4.2.3 on 2023-07-10 14:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('filename', models.CharField(default=None, max_length=255)),
                ('unique_link', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('display_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shared_with', models.ManyToManyField(blank=True, related_name='shared_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
