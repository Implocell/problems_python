from collections import Counter



x = int(input())
y = input().split(" ")
y = [int(y) for y in y]


mean = round(sum(y)/x,1)


def find_median(y):
    y = sorted(y)

    if len(y) % 2 == 0:
        median1 = y[len(y) // 2]
        median2 = y[(len(y) // 2)-1]
        return (median1+median2)/2
    else:
        return y[y // 2]


def find_mode(y):
    mode = dict(Counter(y))
    current_mode = -9999
    current_key = 0
    for key in mode.keys():
        if current_mode == -9999 and mode[key] > 1:
            current_mode = mode[key]
            current_key = key
        elif mode[key] > current_mode and current_mode != -9999:
            current_mode = mode[key]
            current_key = key
        elif mode[key] == current_mode and key < current_key:
            current_key = key
    
    if current_mode == -9999:
        return min(y)
    else:
        return current_mode


median = find_median(y)
mode = find_mode(y)

print(mean)
print(median)
print(mode)