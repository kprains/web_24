from django.db import models

class StudySchedule(models.Model):

    DAY_CHOICES1 = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    subject = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.subject} on {self.day_of_week} from {self.start_time} to {self.end_time})"

class ExtracurricularActivity(models.Model):
    ACTIVITY_CHOICES = [
        ('running', 'Бег'),
        ('swimming', 'Плавание'),
        ('bicycle', 'Велосипед'),
        ('basketball', 'Баскетбол'),
        ('volleyball', 'Волейбол'),
        ('knitting', 'Вязание'),
        ('painting', 'Рисование'),
        ('computer', 'Компьютер'),
        ('friends', 'Друзья'),
        ('TV', 'Телевизор'),
    ]

    DAY_CHOICES = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    activity = models.CharField(max_length=100, choices=ACTIVITY_CHOICES)
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.activity} on {self.day_of_week} from {self.start_time} to {self.end_time}"