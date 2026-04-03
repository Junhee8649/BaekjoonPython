SSN_list, SSN_repeat_set  = [], set()
while True:
    SSN = input()
    if SSN in SSN_list:
        SSN_repeat_set.add(SSN)
        continue
    if SSN == "000-00-0000":
        SSN_repeat_list = sorted(list(SSN_repeat_set))
        for num in SSN_repeat_list:
            print(num)
        break
    SSN_list.append(SSN)