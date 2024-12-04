def time(param):
    hour = param // 3600
    minute = (param - hour * 3600) // 60
    second = param - hour * 3600 - minute * 60
    print (hour, ":", minute, ":", second)

    # hour = param // 3600
    # minute = param % 3600 // 60
    # second = param % 3600 % 60
    # print (hour, ":", minute, ":", second)

time(10000)