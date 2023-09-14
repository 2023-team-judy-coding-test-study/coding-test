import math

def time_calculate(in_time, out_time):
    in_hour, in_minute = list(map(int, in_time.split(':')))
    out_hour, out_minute = list(map(int, out_time.split(':')))
    return (out_hour - in_hour) * 60 + out_minute - in_minute

class Record:
    def __init__(self, in_time):
        self.total_time = 0
        self.check_time = in_time
        self.is_in = True
    
    def car_in(self, in_time):
        self.check_time = in_time
        self.is_in = True
    
    def car_out(self, out_time):
        in_time = self.check_time
        self.total_time += time_calculate(in_time, out_time)
        self.check_time = out_time
        self.is_in = False
    
    def calculate_fee(self, default_time, default_fee, unit_time, unit_fee):
        time = self.total_time - default_time
        if time > 0:
            return default_fee + math.ceil(time / unit_time) * unit_fee
        return default_fee

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    car_record_dict = {}
    
    for record_data in records:
        time, num, act = record_data.split()
        if act == 'IN':
            if num not in car_record_dict:
                car_record_dict[num] = Record(time)
            else:
                car_record_dict[num].car_in(time)
        elif act == 'OUT':
            car_record_dict[num].car_out(time)
            
    car_nums = sorted(car_record_dict.keys())
    answer = []
    
    for num in car_nums:
        record = car_record_dict[num]
        if record.is_in:
            record.car_out('23:59')
        fee = record.calculate_fee(default_time, default_fee, unit_time, unit_fee)
        answer.append(fee)
    
    return answer