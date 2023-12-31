# Generated by Django 4.2.2 on 2023-06-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('jr_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_company', models.CharField(max_length=100)),
                ('total_experience', models.FloatField()),
                ('ctc', models.FloatField()),
                ('expected_ctc', models.FloatField()),
                ('offers_in_hand', models.IntegerField()),
                ('notice_period', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('screened_by', models.CharField(max_length=100)),
                ('source_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('jr_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_company', models.CharField(max_length=100)),
                ('total_experience', models.FloatField()),
                ('ctc', models.FloatField()),
                ('expected_ctc', models.FloatField()),
                ('offers_in_hand', models.IntegerField()),
                ('notice_period', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('screened_by', models.CharField(max_length=100)),
                ('source_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('jr_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_company', models.CharField(max_length=100)),
                ('total_experience', models.FloatField()),
                ('ctc', models.FloatField()),
                ('expected_ctc', models.FloatField()),
                ('offers_in_hand', models.IntegerField()),
                ('notice_period', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('screened_by', models.CharField(max_length=100)),
                ('source_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('jr_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_company', models.CharField(max_length=100)),
                ('total_experience', models.FloatField()),
                ('ctc', models.FloatField()),
                ('expected_ctc', models.FloatField()),
                ('offers_in_hand', models.IntegerField()),
                ('notice_period', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('screened_by', models.CharField(max_length=100)),
                ('source_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('jr_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_company', models.CharField(max_length=100)),
                ('total_experience', models.FloatField()),
                ('ctc', models.FloatField()),
                ('expected_ctc', models.FloatField()),
                ('offers_in_hand', models.IntegerField()),
                ('notice_period', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('screened_by', models.CharField(max_length=100)),
                ('source_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('jr_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('current_company', models.CharField(max_length=100)),
                ('total_experience', models.FloatField()),
                ('ctc', models.FloatField()),
                ('expected_ctc', models.FloatField()),
                ('offers_in_hand', models.IntegerField()),
                ('notice_period', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('screening_status', models.CharField(max_length=100)),
                ('screened_by', models.CharField(max_length=100)),
                ('source_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
