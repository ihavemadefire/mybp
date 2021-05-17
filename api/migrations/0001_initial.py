# Generated by Django 2.2.12 on 2021-05-17 04:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('diastol', models.IntegerField(null=True)),
                ('systol', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Patient')),
            ],
        ),
    ]
