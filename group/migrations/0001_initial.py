# Generated by Django 2.1.5 on 2019-01-21 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('hobbies', models.TextField()),
                ('picture', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChildDisorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_level', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Disorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=200)),
                ('symptom', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='disorder',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Solution'),
        ),
        migrations.AddField(
            model_name='childdisorder',
            name='d_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Disorder'),
        ),
    ]
