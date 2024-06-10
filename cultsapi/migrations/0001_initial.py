# Generated by Django 5.0.6 on 2024-06-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('founder', models.CharField(max_length=255)),
                ('founding_date', models.DateField()),
                ('location', models.TextField()),
                ('symbols', models.TextField()),
                ('core_beliefs', models.TextField()),
                ('rituals_practices', models.TextField()),
                ('hierarchy', models.TextField()),
                ('membership', models.TextField()),
                ('significant_events', models.TextField()),
                ('public_perception', models.TextField()),
                ('controversies', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aliases', models.JSONField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('place_of_death', models.CharField(blank=True, max_length=100, null=True)),
                ('family_background', models.TextField()),
                ('education', models.TextField()),
                ('cult_founded', models.CharField(max_length=100)),
                ('founding_date', models.CharField(max_length=200)),
                ('founding_location', models.CharField(max_length=100)),
                ('core_beliefs', models.TextField()),
                ('symbols', models.TextField()),
                ('leadership_style', models.TextField()),
                ('significant_events', models.TextField()),
                ('controversies', models.TextField()),
                ('followers', models.TextField()),
                ('impact', models.TextField()),
                ('media_coverage', models.TextField()),
                ('personality_traits', models.TextField()),
                ('mental_health', models.TextField(blank=True, null=True)),
                ('criminal_record', models.TextField(blank=True, null=True)),
                ('trials_and_sentences', models.TextField(blank=True, null=True)),
                ('public_perception', models.TextField()),
                ('influence_on_modern_movements', models.TextField()),
            ],
        ),
    ]