import datetime


def your_age(today, birth):
    age = today.year - birth.year
    if birth.month > today.month:
        age += 1
    elif birth.month == today.month:
        if birth.day >= today.day:
            age += 1
    return age


def days_until_birthday(today, birth):
    if birth.strftime('%j') > date.strftime('%j'):
        count = birth.strftime('%j') - today.strftime('%j')
    elif today.strftime('%j') > birth.strftime('%j'):
        count = (365 - int(today.strftime('%j')) )+ int(birth.strftime('%j'))
    else: count = 0
    return count


date = datetime.datetime.today()

birthday = raw_input("Type in your birth date in {Month} {day}, {year} format (ex: January 1, 1999): ")

format = '%B %d, %Y'
birthday = datetime.datetime.strptime(birthday, format)

print 'You are %d years old' % your_age(date,birthday)
print 'Your birthday is in %s days' % days_until_birthday(date,birthday)
