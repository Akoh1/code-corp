# Generated by Django 3.1.4 on 2021-01-11 08:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='QuesComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AnsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.answers')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
    ]