from datetime import datetime as dt, time, datetime
from datetime import timedelta
from time import strftime


class TimeTable:

    dat = None;
    slots = None;

    @classmethod
    def generateTimeTable(self, dat, term):
        self.dat = dat;
        for eachday in dat:
            calendar30days = self.buildTimeTable(eachday,term)

        return calendar30days

    @classmethod
    def getNextDay_(self, day, dat):
        if dat.strftime('%A') == day:
             return dat
        else:
            return datetime.now() + timedelta(days=7)


    @classmethod
    def buildTimeTable(self, dayoftheweek, shifts):
        list_of_next_30days  = {}
        i = 1
        current_date = datetime.now()
        nextDay = self.getNextDay_(dayoftheweek, current_date)
        countDays = 0
        slots = self.getSlotsFromTerms(shifts)
        while i <= 30:
            list_of_next_30days[nextDay + timedelta(days=countDays)] = slots
            countDays = countDays + 7
            i = i+1
        return list_of_next_30days;

    @classmethod
    def getWeekDayN(self, day):
        daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return daysOfWeek.index(day) + 1

    @classmethod
    def getSlotsFromTerms(self, terms):
        slots = []
        for term in terms:
            if term=='1':
                slots.append(TimeTable.getSlots(8,9))
            if term=='2':
                slots.append(TimeTable.getSlots(12,13))
            if term=='3':
                slots.append(TimeTable.getSlots(13,14))

        return slots

    @staticmethod
    def getSlots(fro, to):
        terms = []
        terms.append(str(fro) + ":" + str(to))
        terms.append(str(fro + 1) + ":" + str(to + 1))
        terms.append(str(fro + 2) + ":" + str(to + 2))
        terms.append(str(fro + 2) + ":" + str(to + 2))
        return terms;

    @classmethod
    def getNextDayWeek(self, date_time, dayofweek):
        start_time_w = date_time.isoweekday()
        target_w = self.get_weekday(dayofweek)
        if start_time_w < target_w:
            day_diff = target_w - start_time_w
        else:
            day_diff = 7 - (start_time_w - target_w)

        return date_time + timedelta(days=day_diff)