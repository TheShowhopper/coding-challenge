# 1
# start1, end1
#     []
# Condition 1 cut end_date
# Condition 2 Compare: overlap
#             if: add value for further start_date
#             else: equal start_date, add value for both start_date
# 1: 1------------15                       [(s1,e1):0]
# 2:           14------------------31      [(s1,e1):0,(s2,e2):1]
# 3:                   16----------31      [(s1,e1):0,(s2,e2):1,(s3,e3):1]
# 4:       7-----------16                  [(s1,e1):0,(s2,e2):2,(s3,e3):2,(s4,e4):1]
# 5: 1-----------------------------31      [(s1,e1):1,(s2,e2):3,(s3,e3):3,(s4,e4):2,(s5,e5):1]
# 6:         10----------->20              [(s1,e1):1,(s2,e2):4,(s3,e3):4,(s4,e4):3,(s5,e5):1,(s6,e6):2]
# 7:                       20-->21         [(s1,e1):1,(s2,e2):4,(s3,e3):4,(s4,e4):3,(s5,e5):1,(s6,e6):2,(s7,e7):4]
# 14,16,20 --->14

from datetime import datetime, timedelta


class DateRange:
    def __init__(self, start, end):
        self.start = datetime.strptime(start, '%Y-%m-%d')
        self.end = datetime.strptime(end, '%Y-%m-%d') - timedelta(days=1)
        self.count_overlap = 0

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if self.count_overlap == other.count_overlap:
            return self.start > other.start  # get less than when inverse
        return self.count_overlap < other.count_overlap

    def __str__(self):
        return "{} to {}: {}".format(self.start.strftime('%Y-%m-%d'), self.end.strftime('%Y-%m-%d'), self.count_overlap)

    def getStartDate(self):
        return self.start.strftime('%Y-%m-%d')

    def isOverlapped(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        latest_start = max(self.start, other.start)
        earliest_end = min(self.end, other.end)
        delta = (earliest_end - latest_start).days + 1
        overlap = max(0, delta)
        return overlap > 0

    # def __cmp__(self, other):
    #     assert isinstance(other, A) # assumption for this example
    #     return cmp((self.name, self.age, self.other),
    #             (other.name, other.age, other.other))


# Data Set for sample
raw1 = [("2020-01-01", "2020-01-16"),
        ("2020-01-14", "2020-02-01"),
        ("2020-01-16", "2020-02-01"),
        ("2020-01-07", "2020-01-17"),
        ("2020-01-01", "2020-02-01"),
        ("2020-01-10", "2020-01-21"),
        ("2020-01-20", "2020-01-22")]
# Key Raw 1 = 2020-05-14
raw2 = [("2020-01-01", "2020-04-30"),
        ("2020-04-28", "2020-06-30"),
        ("2020-05-01", "2020-05-30"),
        ("2021-05-01", "2021-05-30"),
        ("2020-05-28", "9999-05-30")]
# Key Raw 2 = 2020-05-28

raw = []
n = int(input("N: "))
for i in range(n):
    start, end = input().split()
    raw.append(start, end)

data = [DateRange(start, end) for start, end in raw]

for i in range(len(data)):
    for j in range(i):  # i get [0,1,2,..,i-1]
        overlap = data[i].isOverlapped(data[j])
        if overlap:
            if data[i].start == data[j].start:
                data[i].count_overlap += 1
                data[j].count_overlap += 1
            elif data[i].start > data[j].start:
                data[i].count_overlap += 1
            else:
                data[j].count_overlap += 1


data.sort(reverse=True)
print(data[0].getStartDate())
