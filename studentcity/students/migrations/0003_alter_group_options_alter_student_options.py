# Generated by Django 4.1.3 on 2024-11-19 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_group_id_student_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
    ]
