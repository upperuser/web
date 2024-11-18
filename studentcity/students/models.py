from django.db import models
from datetime import date

class City(models.Model):
    name = models.CharField(verbose_name='Название', max_length=25)
class Student(models.Model):
    objects = None
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)
    curs = models.IntegerField(verbose_name='Курс',)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа', null=True)
    record_book = models.IntegerField(verbose_name='Номер зачетной книжки',)
    birth_date = models.DateField(verbose_name='Дата рождения', default=date(2000,1,1))

class CheckIn(models.Model):
    check_in_date = models.DateField(verbose_name='Дата заселения', default=date(2000,1,1))
    eviction_date = models.DateField(verbose_name='Дата выселения', default=date(2000,1,1))
    costs = models.IntegerField(verbose_name='Стоимость',)
class Room(models.Model):
    number_room = models.SmallIntegerField(verbose_name='Номер комнаты',)
    check_in_count = models.IntegerField(verbose_name='Количество заселенных',)
class Dormitory(models.Model):
    number_dormitory = models.SmallIntegerField(verbose_name='Номер общежития',)
    place_dormitory = models.CharField(verbose_name='Адрес', max_length=500)
    seats = models.SmallIntegerField(verbose_name='Количество мест',)


class Group(models.Model):
    name = models.CharField(verbose_name='Группа', max_length=5)
    course = models.CharField(verbose_name='Курс', max_length=2)
    enrollment_year = models.IntegerField(verbose_name='Год зачисления')
    def __str__(self):
        return f'{self.course}-{self.name}'

