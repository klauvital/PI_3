from datetime import datetime, timedelta

from django import template

register = template.Library()


@register.filter('duration_to_hours')
def duration_to_hours(value):
    '''
    Converte duration em horas.
    '''
    if value < timedelta(hours=24):
        return datetime.strftime(datetime.strptime(str(value), '%H:%M:%S'), '%H:%M:%S')

    elif value == timedelta(hours=24):
        return '24:00:00'

    elif value < timedelta(hours=48):
        dias = datetime.strftime(datetime.strptime(str(value), '%d day, %H:%M:%S'), '%d')
        horas_restantes = datetime.strftime(datetime.strptime(str(value), '%d day, %H:%M:%S'), '%H')
        resto = datetime.strftime(datetime.strptime(str(value), '%d day, %H:%M:%S'), '%M:%S')
        return f'{int(dias) * 24 + int(horas_restantes)}:{resto}'

    dias = datetime.strftime(datetime.strptime(str(value), '%d days, %H:%M:%S'), '%d')
    horas_restantes = datetime.strftime(datetime.strptime(str(value), '%d days, %H:%M:%S'), '%H')
    resto = datetime.strftime(datetime.strptime(str(value), '%d days, %H:%M:%S'), '%M:%S')
    return f'{int(dias) * 24 + int(horas_restantes)}:{resto}'
