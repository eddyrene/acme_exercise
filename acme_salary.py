
import sys

days_table = ['MO','TU','WE','TH','FR','SA','SU']
salary_table =  [[25,15,25],
                [25,15,25],
                [25,15,25],
                [25,15,25],
                [25,15,25],
                [30,20,25],
                [30,20,25]]

#define a function to get hours of the day
def get_hours(text):
    ini, fin = text.split('-')
    ini = int(ini.split(':')[0])
    fin = int(fin.split(':')[0])
    return list(range(ini,fin))

def get_salary_hour(hour,salary_list):
    salary = 0
    if hour >= 0 and hour < 9:
        salary = salary_list[0]
    elif hour >= 9 and hour < 18:
        salary = salary_list[1]
    else: 
        salary = salary_list[2]
    return salary

def calc_salary_day(day_s, hours_s):
    d_index = days_table.index(day_s)
    return sum([get_salary_hour( h , salary_table[d_index]) for h in  hours_s ])

def calc_total_salary(text_input):
    user, schedule  = text_input.split('=')
    schedule = schedule.split(',')
    user, schedule

    days_list = [item[:2] for item in schedule]
    hours = [item[2:] for item in schedule]
    hours_list = [get_hours(item) for item in hours]

    salary = 0
    for idx, val in enumerate(days_list):
        salary = salary + calc_salary_day(days_list[idx],hours_list[idx])
    output = "The amount to pay "+user+" is: " + str(salary) + " USD"
    return output


if __name__ == '__main__':
    try:
        print(calc_total_salary(sys.argv[1]))
    except:
        print('Invalid input')