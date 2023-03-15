# Generated by Django 4.1.1 on 2023-03-15 06:19

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidate', '0001_initial'),
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=30)),
                ('total_cost', models.IntegerField()),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='uploads/', verbose_name='Image')),
                ('prize', models.CharField(blank=True, max_length=19, null=True)),
                ('is_draw', models.BooleanField(default=False)),
                ('seller_number', models.IntegerField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lottery_bill', to='candidate.candidate')),
                ('period', models.ManyToManyField(to='period.period')),
            ],
        ),
    ]
