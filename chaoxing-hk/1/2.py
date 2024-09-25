# 输出2000~3000的所有闰年

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# 18 个一行
leap_years = [year for year in range(2000, 3001) if is_leap_year(year)]
for i in range(0, len(leap_years), 18):
    print(*leap_years[i:i+18])
