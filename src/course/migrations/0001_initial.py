# Generated by Django 2.2.7 on 2019-12-07 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kg_name', models.CharField(max_length=200, verbose_name='Имя на кыргызском')),
                ('ru_name', models.CharField(max_length=200, verbose_name='Имя на русском')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('kg', 'Кыргызча')], max_length=2, verbose_name='Язык проведения')),
                ('name_kg', models.CharField(max_length=200, verbose_name='На кыргызском')),
                ('name_ru', models.CharField(max_length=200, verbose_name='На русском')),
                ('description_kg', models.TextField(verbose_name='На кыргызском')),
                ('description_ru', models.TextField(verbose_name='На русском')),
                ('image', models.ImageField(upload_to='course/', verbose_name='Изображение')),
                ('registration_link', models.CharField(max_length=200, verbose_name='Ссылка на регистрацию')),
                ('start', models.DateField(verbose_name='Начало')),
                ('end', models.DateField(verbose_name='Конец')),
                ('available', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('kg', 'Кыргызча')], max_length=2, verbose_name='Язык преподования')),
                ('about_kg', models.TextField(verbose_name='О препод. на кыргызском')),
                ('about_ru', models.TextField(verbose_name='О препод. на русском')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Преподователь',
                'verbose_name_plural': 'Преподователи',
            },
        ),
        migrations.CreateModel(
            name='VideoLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_kg', models.CharField(max_length=500, verbose_name='Описание(Kg)')),
                ('description_ru', models.CharField(max_length=500, verbose_name='Описание(Ru)')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
            options={
                'verbose_name': 'Видео курса',
                'verbose_name_plural': 'Видео курса',
            },
        ),
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Понидельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], verbose_name='День недели')),
                ('time', models.TimeField(verbose_name='Время')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Расписание курса',
            },
        ),
        migrations.CreateModel(
            name='ProgramItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Программы курса',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_kg', models.CharField(max_length=500, verbose_name='Описание(Kg)')),
                ('description_ru', models.CharField(max_length=500, verbose_name='Описание(Ru)')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы круса',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Teacher', verbose_name='Преподователь'),
        ),
    ]