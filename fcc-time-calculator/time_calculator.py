hours_24_format = {str(x): str(12 + x) for x in range(1, 12)}
hours_24_format['12'] = '00'

hours_12_format = {str(12 + x): str(x) for x in range(1, 12)}
hours_12_format['12'] = '12'

days_of_the_week = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7
}

rev_days_of_the_week = {y: x for (x, y) in days_of_the_week.items()}
#6:10 PM
output_only_hours = "{}"

#2:02 PM, Monday
output_hours_dow = "{}, {}"

#1:40 AM (next day)
output_hours_days = "{} {}"

#12:03 AM, Thursday (2 days later)
output_all = "{}, {} {}"


def get_minutes_and_hours(start_minutes, duration_minutes):
    start_minutes = int(start_minutes)
    duration_minutes = int(duration_minutes)
    total_minutes = start_minutes + duration_minutes
    if total_minutes % 60 == 0:
        minutes = 0
    else:
        minutes = total_minutes % 60
    hours = total_minutes // 60

    return {'hours': hours, 'minutes': minutes}


def get_number_of_days(total_hours):
    day_s = total_hours // 24
    message = ('', 0)
    if day_s == 1:
        message = ('(next day)', day_s)
    elif day_s > 1:
        message = ('({} days later)'.format(day_s), day_s)
    return message


def get_day_of_the_week(days=0, start='monday'):
    dow = days_of_the_week[start]
    for x in range(days):
        dow += 1
        if dow == 7:
            dow = 0
    if dow == 0:
        dow = 7
    #print(rev_days_of_the_week[dow].title())
    return rev_days_of_the_week[dow].title()


def add_time(start, duration, dow=None):
    new_time = ''
    hours_and_minutes = get_minutes_and_hours(
        start.split(':')[1].split()[0],
        duration.split(':')[1])
    pm_or_am = start.split(':')[1].split()[1]
    total_hours = 0
    if pm_or_am == 'PM' and start.split(':')[0] != 12:
        total_hours = int(hours_24_format[start.split(':')[0]]) + int(
            duration.split(':')[0]) + hours_and_minutes['hours']
    else:
        total_hours = int(start.split(':')[0]) + int(
            duration.split(':')[0]) + hours_and_minutes['hours']
    next_hours = str(total_hours % 24)
    #print("next_hours: {}".format(next_hours))
    if int(next_hours) >= 12:
        #print("{}:{:02d} {}".format(hours_12_format[next_hours],hours_and_minutes['minutes'], 'PM'))
        current_hour = "{}:{:02d} {}".format(
            hours_12_format[next_hours], hours_and_minutes['minutes'], 'PM')
    elif int(next_hours) == 0:
        #print("{}:{:02d} {}".format(12, hours_and_minutes['minutes'], 'AM'))
        current_hour = "{}:{:02d} {}".format(12, hours_and_minutes['minutes'],
                                             'AM')
    else:
        #print("{}:{:02d} {}".format(next_hours, hours_and_minutes['minutes'],'AM'))
        current_hour = "{}:{:02d} {}".format(
            next_hours, hours_and_minutes['minutes'], 'AM')

    #print(get_number_of_days(total_hours)[0])
    if dow:
        dow = get_day_of_the_week(
            get_number_of_days(total_hours)[1], dow.lower())

    number_of_days = get_number_of_days(total_hours)[0]

    if current_hour:
        new_time = output_only_hours.format(current_hour)
    if current_hour and number_of_days:
        new_time = output_hours_days.format(current_hour, number_of_days)
    if current_hour and dow:
        new_time = output_hours_dow.format(current_hour, dow)
    if current_hour and dow and number_of_days:
        new_time = output_all.format(current_hour, dow, number_of_days)
  
    return new_time.rstrip()
