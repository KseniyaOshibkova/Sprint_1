time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_intervals = time.split(',')
total_time = 0

for interval in time_intervals:
    time_parts = interval.split()
    for part in time_parts:
        if part[-1] == 's':
            total_time += int(part[:-1]) / 60
        elif part[-1] == 'm':
            total_time += int(part[:-1])
        elif part[-1] == 'h':
            total_time += int(part[:-1]) * 60
        print(part)
    print('Общее количество минут:', total_time)
