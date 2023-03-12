from collections import defaultdict


def caltime(t1, t2):
    h1, m1, s1 = map(int, t1.split(":"))
    h2, m2, s2 = map(int, t2.split(":"))
    total_seconds = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return str(hours)+":"+str(minutes)+":"+str(seconds)


def sumtime(timelist):
    total_seconds = 0
    for i in timelist:
        h, m, s = map(int, i.split(":"))
        total_seconds += (h) * 3600 + (m) * 60 + (s)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return str(hours)+":"+str(minutes)+":"+str(seconds)


def avgtime(time, totalemployes):
    h, m, s = map(int, time.split(":"))
    return str(h//totalemployes)+":"+str(m//totalemployes)+":"+str(s//totalemployes)


def besttime(timelist):
    bsttime = "0:0:0"
    for i in timelist:
        h1, m1, s1 = map(int, i.split(":"))
        h2, m2, s3 = map(int, bsttime.split(":"))
        if h1 > h2:
            bsttime = i
        elif h2 > h1:
            pass
        elif m1 > m2:
            bsttime = i
        elif m1 < m2:
            pass
        elif s1 > s2:
            bsttime = i
        elif s1 < s2:
            pass
    return bsttime


def worsttime(timelist):
    wrttime = timelist[0]
    for i in timelist:
        h1, m1, s1 = map(int, i.split(":"))
        h2, m2, s2 = map(int, wrttime.split(":"))
        if h1 < h2:
            wrttime = i
        elif h2 < h1:
            pass
        elif m1 < m2:
            wrttime = i
        elif m1 > m2:
            pass
        elif s1 < s2:
            wrttime = i
        elif s1 > s2:
            pass
    return wrttime


if __name__ == "__main__":
    inp = open("TT_large.txt", 'r')
    out = open("TT_large_Output.txt", 'w')
    data = inp.readlines()
    testcases = int(data[0])
    uniquemonths = []
    uniqueEmp = []
    MonthData = defaultdict(list)
    for _ in range(1, testcases+1):
        templist = list(map(str, data[_].split()))
        tempstring = str(templist[3])
        l = defaultdict()
        l = {'EMP': (templist[0]), 'Date': (templist[1]),
             tempstring: (templist[2])}
        # EmpData[templist[0]].append(l)
        if templist[1][5:7] not in uniquemonths:
            uniquemonths.append(templist[1][5:7])
        if templist[0] not in uniqueEmp:
            uniqueEmp.append(templist[0])
        MonthData[templist[0]+","+templist[1]].append(l)
    # print("all unique months",uniquemonths)
    # print("all unique EMP", uniqueEmp)
    res = []
    EmpData = defaultdict(list)
    for k, v in MonthData.items():
        # print(k)
        ckin, ckout, bksrt, bkstp = "0"*4
        for j in v:
            for jk, jv in j.items():
                if jk == "clock-in":
                    ckin = jv
                elif jk == "clock-out":
                    ckout = jv
                elif jk == "break-start":
                    bksrt = jv
                elif jk == "break-stop":
                    bkstp = jv
                # print(jk, jv)
        breaktime = caltime(bksrt, bkstp)
        totaltime = ""
        if ckout == "0":
            temp1 = caltime(ckin, "19:30:00")
            temp2 = "6:00:00"
            h1, m1, s1 = map(int, temp1.split(":"))
            h2, m2, s2 = map(int, temp2.split(":"))
            if h1 > h2:
                totaltime = temp2
            elif h2 > h1:
                totaltime = temp1
            elif m1 > m2:
                totaltime = temp2
            elif m1 < m2:
                totaltime = temp1
            elif s1 > s2:
                totaltime = temp2
            elif s1 < s2:
                totaltime = temp1
        else:
            totaltime = caltime(ckin, ckout)
        Worktime = caltime(breaktime, totaltime)
        # print("ckin:", ckin, "ckout:", ckout, "bksrt:", bksrt, "bkstop:", bkstp, "Totaltime:", totaltime, "breaktime:",
        #       breaktime, "Worktime:", Worktime)
        # print("breaktime: ", breaktime)
        # print("Worktime: ", Worktime)
        EmpData[k[0:5]+","+k[11:13]].append(Worktime)
        res.append(Worktime)
    # print(res)
    # print(EmpData)
    total_working_time = []
    for k, v in EmpData.items():
        timesum = sumtime(v)
        # print(k, timesum)
        total_working_time.append(timesum)
    BestTime = besttime(total_working_time)
    WorstTime = worsttime(total_working_time)
    AvgTime = avgtime(sumtime(total_working_time), len(uniqueEmp))
    out.write("Case #1: {0}, {1}, {2}\n".format(BestTime, WorstTime, AvgTime))
