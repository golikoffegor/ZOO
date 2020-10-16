from django.db import models


class Animal(models.Model):
    WILD = 'wild'
    CHANGING = 'changing'
    PEACEFUL = 'peaceful'

    TEMPER_TYPE = [
        (WILD, 'Буйный'),
        (CHANGING, 'Переменчивый'),
        (PEACEFUL, 'Спокойный'),
    ]

    nickname = models.CharField(max_length = 128, verbose_name = 'порода')
    name = models.CharField(max_length = 128, verbose_name = 'кличка')
    temper = models.CharField(max_length = 128, choices = TEMPER_TYPE, verbose_name = 'характер')
    age = models.IntegerField(verbose_name = 'возраст в годах')
    description = models.TextField(max_length = 300,blank = True, null = True, verbose_name = 'описание')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'зарегестрирован')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "животное"
        verbose_name_plural = "животные"

class Animal_Type(models.Model):
    PREDATOR = 'predator'
    HERBIVORIOUS = 'herbivorous'
    OMNIVOROUS = 'omnivorous'

    CHOICES_TYPE = [
        (PREDATOR, 'Хищник'),
        (HERBIVORIOUS, 'Травоядный'),
        (OMNIVOROUS, 'Всеядный'),
    ]

    YES = 'yes'
    NO = 'no'

    Y_N_TYPE = [
        (YES, 'Да'),
        (NO, 'Нет'),
    ]

    name = models.ForeignKey('Animal', on_delete = models.CASCADE, verbose_name = 'животное')
    animal_type = models.CharField(max_length = 128, choices = CHOICES_TYPE, verbose_name = 'тип питания')
    safe_feeding = models.CharField(max_length = 128, choices = Y_N_TYPE, verbose_name = 'безопасное кормление')
    independence = models.CharField(max_length = 128, choices = Y_N_TYPE, verbose_name = 'самостоятельное питание')
    description = models.TextField(max_length = 300,blank = True, null = True, verbose_name = 'описание')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'зарегестрирован')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "животного с определенным типом питания"
        verbose_name_plural = "животные по типу питания"

class Animal_Place(models.Model):
    CELL = 'cell'
    ENCLOSURE = 'enclosure'
    TERRARIUM = 'terrarium'

    PLACE_TYPE = [
        (CELL, 'Клетка'),
        (ENCLOSURE, 'Вольер'),
        (TERRARIUM, 'Террариум'),
    ]

    HEATABLE = 'heatable'
    UNHEATED = 'unheated'

    HEAT_TYPE = [
        (HEATABLE, 'Отапливаемый'),
        (UNHEATED, 'Неотапливаемый'),
    ]
    
    name = models.CharField(max_length = 128, verbose_name = 'название места содержания')
    nickname_1 = models.ForeignKey('Animal', blank = True, null = True, on_delete = models.SET_NULL, related_name = 'nickname_1', verbose_name = 'Выберите животное #1')
    nickname_2 = models.ForeignKey('Animal', blank = True, null = True, on_delete = models.SET_NULL, related_name = 'nickname_2', verbose_name = 'Выберите животное #2')
    nickname_3 = models.ForeignKey('Animal', blank = True, null = True, on_delete = models.SET_NULL, related_name = 'nickname_3', verbose_name = 'Выберите животное #3')
    place_type = models.CharField(max_length = 128, choices = PLACE_TYPE, verbose_name = 'тип содержания')
    heat = models.CharField(max_length = 128, choices = HEAT_TYPE, verbose_name = 'отопление')
    description = models.TextField(max_length = 300,blank = True, null = True, verbose_name = 'описание')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'зарегестрирован')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "животного с определенным местом содержания"
        verbose_name_plural = "места содержания животных"

class Staff(models.Model):
    FEMALE = 'female'
    MALE = 'male'

    GENDER_CHOICES = [
        (FEMALE, 'Женский'),
        (MALE, 'Мужской'),
    ]

    name = models.CharField(max_length = 128, verbose_name = 'имя сотрудника')
    gender = models.CharField(max_length = 128, choices = GENDER_CHOICES, verbose_name = 'пол')
    protected_animal = models.ForeignKey('Animal', blank = True, null = True, on_delete = models.SET_NULL, verbose_name = 'наблюдаемое животное')
    protection_time = models.IntegerField(verbose_name = 'время наблюдения (дней)')
    description = models.TextField(max_length = 300,blank = True, null = True, verbose_name = 'описание')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'зарегестрирован')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"


