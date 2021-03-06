# Generated by Django 3.1.6 on 2021-02-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_tests', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Pizza',
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_tests.pizza')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
