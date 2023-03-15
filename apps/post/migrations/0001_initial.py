# Generated by Django 4.1.1 on 2023-03-15 06:19

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('address', models.TextField()),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='', verbose_name='Image')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='period.period')),
            ],
        ),
    ]
