# Generated by Django 4.2.4 on 2023-10-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_crete_at_experience_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecole', models.CharField(max_length=100)),
                ('diplome', models.CharField(max_length=100)),
                ('Domaine_etude', models.CharField(max_length=100)),
                ('Date_debut', models.DateField()),
                ('année_reussi', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
