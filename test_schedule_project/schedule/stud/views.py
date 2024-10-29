from django.shortcuts import render
from .models import StudySchedule, ExtracurricularActivity

def timetable_view(request):
    # Получаем все занятия и внеучебные активности
    study_schedules = StudySchedule.objects.all().order_by('day_of_week', 'start_time')
    extracurricular_activities = ExtracurricularActivity.objects.all().order_by('day_of_week', 'start_time')

    # Группируем данные по дням недели
    timetable = {
        'monday': [],
        'tuesday': [],
        'wednesday': [],
        'thursday': [],
        'friday': [],
        'saturday': [],
        'sunday': [],
    }

    # Словарь для перевода дней недели
    days_translation = {
        'monday': 'Понедельник',
        'tuesday': 'Вторник',
        'wednesday': 'Среда',
        'thursday': 'Четверг',
        'friday': 'Пятница',
        'saturday': 'Суббота',
        'sunday': 'Воскресенье',
    }

    # Добавляем уроки в расписание
    for schedule in study_schedules:
        timetable[schedule.day_of_week].append({
            'type': 'lesson',
            'subject': schedule.subject,
            'start_time': schedule.start_time,
            'end_time': schedule.end_time,
        })

    # Добавляем внеучебные активности в расписание
    for activity in extracurricular_activities:
        timetable[activity.day_of_week].append({
            'type': 'activity',
            'activity': activity.get_activity_display(),  # Используем get_activity_display()
            'start_time': activity.start_time,
            'end_time': activity.end_time,
        })

    # Сортируем занятия по времени для каждого дня
    for day in timetable:
        timetable[day].sort(key=lambda x: x['start_time'])

    # Переводим дни недели на русский язык
    translated_timetable = {}
    for day in timetable:
        translated_day = days_translation.get(day, day)  # Получаем перевод дня
        translated_timetable[translated_day] = timetable[day]  # Создаем новый словарь с переводом

    return render(request, 'schedule.html', {'timetable': translated_timetable})
