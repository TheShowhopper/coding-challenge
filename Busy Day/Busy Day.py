from datetime import datetime
from datetime import timedelta


def add_booking(start, end):
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    day = (end_date - start_date).days

    for i in range(day):
        date = start_date + timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        if date_str in booking:
            booking[date_str] += 1
        else:
            booking[date_str] = 1


booking = dict()
inputs1 = [("2020-01-01", "2020-04-30"),
           ("2020-04-28", "2020-06-30"),
           ("2020-05-01", "2020-05-30"),
           ("2021-05-01", "2021-05-30"),
           ("2020-05-28", "9999-05-30")]

# for start, end in inputs1:
#     add_booking(start, end)

n = int(input("N: "))
for i in range(n):
    start, end = input().split()
    add_booking(start, end)

# tuples from arraylist(dict)
result = [(-v, k) for k, v in list(booking.items())]
result.sort()
print(result[0][1])
