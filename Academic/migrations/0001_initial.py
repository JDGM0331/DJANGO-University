# Generated by Django 3.2.8 on 2022-09-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Imagen')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('duration', models.PositiveSmallIntegerField(default=5, verbose_name='Duración (años)')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Código')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('credits', models.PositiveSmallIntegerField(verbose_name='Créditos')),
                ('professor', models.CharField(max_length=100, verbose_name='Docente')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('identification', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identificación')),
                ('paternalSurname', models.CharField(max_length=35, verbose_name='Apellido paterno')),
                ('maternalSurname', models.CharField(max_length=35, verbose_name='Apellido materno')),
                ('names', models.CharField(max_length=35, verbose_name='Nombres')),
                ('dateBirth', models.DateField(verbose_name='Fecha de nacimento')),
                ('sex', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1, verbose_name='Sexo')),
                ('validity', models.BooleanField(default=True, verbose_name='Vigencia')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.career', verbose_name='Carrera')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('enrollmentDate', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de matriculación')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.course', verbose_name='Curso')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.student', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matrículas',
            },
        ),
    ]
