import random
IS_PRESENT = 1
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

def get_work_hours():

    emp_check = random.randint(0,1)
    if emp_check == IS_PRESENT:
        work_hrs = FULL_DAY_HOUR

    else:
        work_hrs = 0
    return work_hrs

daily_emp_wage = WAGE_PER_HOUR * get_work_hours()
print(f"Person Earn  {daily_emp_wage} Rupees this day")

