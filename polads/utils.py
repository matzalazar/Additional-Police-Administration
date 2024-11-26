import calendar
from calendar import HTMLCalendar, LocaleHTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc

class CalendarioTurnos(LocaleHTMLCalendar):

    def __init__(self, turnos, locale):
        super(CalendarioTurnos, self).__init__(locale='es_ES.utf8')
        self.turnos = self.group_by_day(turnos)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.turnos:
                cssclass += ' filled'
                body = ['<ul>']
                for turno in self.turnos[day]:
                    body.append('- ')
                    body.append(esc(turno.ingreso.hour))
                    body.append(':00')
                    body.append(' a ')
                    if turno.egreso.hour == 00:
                        body.append('24:00')
                    else:
                        body.append(esc(turno.egreso.hour))
                    body.append(':00 ')
                    body.append(esc(turno.efectivo.efectivo_nombre.split(' ', 1)[0]))
                    body.append('<br />')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(CalendarioTurnos, self).formatmonth(year, month)


    def group_by_day(self, turnos):
        field = lambda turno: turno.ingreso.day
        return dict(
            [(day, list(items)) for day, items in groupby(turnos, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
