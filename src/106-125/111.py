monthdic = dict(zip(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], [
                '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
n = int(input())
for i in range(n):
    mon, day, year = input().split()
    day = '{:02d}'.format(int(day[:-1]))
    year = '{:04d}'.format(int(year))
    mon = monthdic[mon]
    date = year + mon + day
    print('Y' if date == date[::-1] else 'N', date)
