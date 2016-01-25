# Hint:  use Google to find python function
from datetime import *

def time_between_dates1(date_start, date_stop):
    start_date = date(int(date_start[-4:]), int(date_start[:2]), int(date_start[3:5]))
    end_date = date(int(date_stop[-4:]), int(date_stop[:2]), int(date_stop[3:5]))
    return (end_date - start_date).days

def time_between_dates2(date_start, date_stop):
    start_date = date(int(date_start[4:]), int(date_start[:2]), int(date_start[2:4]))
    end_date = date(int(date_stop[4:]), int(date_stop[:2]), int(date_stop[2:4]))
    return (end_date - start_date).days


def month_converter(month):
    month_dict = {'Jan':1,
                  'Feb':2,
                  'Mar':3,
                  'Apr':4,
                  'May':5,
                  'Jun':6,
                  'Jul':7,
                  'Aug':8,
                  'Sep':9,
                  'Oct':10,
                  'Nov':11,
                  'Dec':12}
    return month_dict[month]


def time_between_dates3(date_start, date_stop):
    start_date = date(int(date_start[-4:]), month_converter(date_start[3:6]), int(date_start[:2]))
    end_date = date(int(date_stop[-4:]), month_converter(date_stop[3:6]), int(date_stop[:2]))
    return (end_date - start_date).days


if __name__ == '__main__':
    #a)
    date_start1 = '01-02-2013'
    date_stop1 = '07-28-2015'
    days1 = time_between_dates1(date_start1, date_stop1)
    print 'The answer to a) is ' + str(days1) + ' days.'

    #b)
    date_start2 = '12312013'
    date_stop2 = '05282015'
    days2 = time_between_dates2(date_start2, date_stop2)
    print 'The answer to b) is ' + str(days2) + ' days.'

    #c)
    date_start3 = '15-Jan-1994'
    date_stop3 = '14-Jul-2015'
    days3 = time_between_dates3(date_start3, date_stop3)
    print 'The answer to c) is ' + str(days3) + ' days.'
