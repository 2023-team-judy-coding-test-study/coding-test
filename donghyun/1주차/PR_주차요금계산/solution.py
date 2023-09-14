import math


class ParkInfo:

    def __init__(self, num, status, i="", o="", total_time=0):
        self.num = num
        self.i = i
        self.o = o
        self.status = status
        self.total_time = total_time

    def make_total_time(self):
        if not self.i.__contains__(":") or not self.o.__contains__(":"):
            return

        in_hour, in_min = map(int, self.i.split(":"))
        in_time = in_hour * 60 + in_min

        out_hour, out_min = map(int, self.o.split(":"))
        out_time = out_hour * 60 + out_min

        self.total_time += (out_time - in_time)

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return f"{self.__dict__}"


def solution(fees, records):

    result = {}

    for rec in records:
        time, num, status = rec.split()

        if status == "IN":
            if result.get(num) is None:
                result[num] = ParkInfo(num=num, i=time, status=status)
                continue

            park_info = result[num]
            park_info.i = time
            park_info.status = status
            park_info.o = ""

        elif status == "OUT":
            park_info = result[num]
            park_info.o = time
            park_info.make_total_time()

    for car_num, park_info in result.items():
        if park_info.i and not park_info.o:
            park_info.o = "23:59"
            park_info.status = "OUT"
            park_info.make_total_time()

    total_time_list = [[int(key), value.total_time]
                       for key, value in result.items()]

    total_time_list.sort(key=lambda x: x[0])

    answer = []
    for total_time in total_time_list:
        fee = fees[1]
        if total_time[1] > fees[0]:
            advantage = math.ceil(
                (total_time[1] - fees[0]) / fees[2]) * fees[3]
            fee += advantage
        answer.append(int(fee))

    return answer
