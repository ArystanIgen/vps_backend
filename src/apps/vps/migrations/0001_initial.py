# Generated by Django 4.0.8 on 2022-10-27 20:09

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPSModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('cpu', models.PositiveIntegerField(default=0, verbose_name='Количество Ядер')),
                ('ram', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Объем RAM')),
                ('hdd', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Объем HDD')),
                ('status', models.CharField(choices=[('STARTED', 'Запущен'), ('BLOCKED', 'Заблокирован'), ('STOPPED', 'Остановлен')], default='STOPPED', max_length=32, verbose_name='Статус Сервера')),
            ],
            options={
                'verbose_name': 'VPS',
                'verbose_name_plural': " VPS's ",
            },
        ),
    ]
