def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

answer = leap_year(2020)
print(f'Is that year leap? {answer}')