# Generated by Django 4.2.8 on 2023-12-08 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patman', '0002_admin_calender_diagnosis_excertherapy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('authority_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=70)),
                ('register_date', models.DateTimeField()),
                ('revise_date', models.DateTimeField(blank=True, null=True)),
                ('remove_y', models.IntegerField()),
            ],
            options={
                'db_table': 'authority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorAuthority',
            fields=[
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.doctor')),
            ],
            options={
                'db_table': 'doctor_authority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('equipment_kind', models.CharField(max_length=50)),
                ('equipment_location', models.CharField(max_length=50)),
                ('use_equipment', models.IntegerField()),
            ],
            options={
                'db_table': 'equipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inbody',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.patient')),
                ('inbody_id', models.CharField(max_length=50)),
                ('measure_date', models.DateTimeField()),
                ('patient_weight', models.CharField(max_length=30)),
                ('body_fat_percentage', models.CharField(max_length=30)),
                ('muscle_mass', models.CharField(max_length=30)),
                ('basal_metabolism', models.CharField(max_length=30)),
                ('fatness_index', models.CharField(max_length=30)),
                ('aqua', models.CharField(max_length=30)),
                ('obesity_scale', models.CharField(max_length=30)),
                ('unit_analysis', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'inbody',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagerAuthority',
            fields=[
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.admin')),
            ],
            options={
                'db_table': 'manager_authority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NokAuthority',
            fields=[
                ('protector', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.nok')),
            ],
            options={
                'db_table': 'nok_authority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NurseAuthorization',
            fields=[
                ('nurse', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.nurse')),
            ],
            options={
                'db_table': 'nurse_authorization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientAuthority',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.patient')),
            ],
            options={
                'db_table': 'patient_authority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.patient')),
                ('allergy', models.CharField(blank=True, max_length=30, null=True)),
                ('disease', models.CharField(blank=True, max_length=30, null=True)),
                ('symptom', models.CharField(blank=True, max_length=20, null=True)),
                ('symptom_period', models.CharField(blank=True, max_length=17, null=True)),
                ('reh_status', models.IntegerField(blank=True, null=True)),
                ('disable_status', models.CharField(max_length=50)),
                ('smoke_period', models.CharField(blank=True, max_length=30, null=True)),
                ('drink', models.IntegerField(blank=True, null=True)),
                ('exercise', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'questionnaire',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RehabilitationEquipment',
            fields=[
                ('reh_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('reh_equipment_type', models.CharField(max_length=50)),
                ('reh_equipment_location', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rehabilitation_equipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TherapistAuthority',
            fields=[
                ('therapist', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.therapist')),
            ],
            options={
                'db_table': 'therapist_authority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Xray',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.patient')),
                ('staff_id', models.CharField(max_length=255)),
                ('shooting_date', models.DateTimeField()),
                ('shooting_equipment', models.CharField(blank=True, max_length=255, null=True)),
                ('shooting_part', models.CharField(blank=True, max_length=255, null=True)),
                ('xray_type', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor_opinion', models.TextField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'xray',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EquipmentRental',
            fields=[
                ('equipment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.equipment')),
                ('rental_period', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'equipment_rental',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UseRehabilitationEquipment',
            fields=[
                ('reh', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='patman.rehabilitationequipment')),
                ('use_reh_equipment', models.IntegerField()),
            ],
            options={
                'db_table': 'use_rehabilitation_equipment',
                'managed': False,
            },
        ),
    ]
