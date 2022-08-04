startw = input("Enter start week")
endw = input("Enter end week")
temp = []
with open('yearTemperatures.txt','r') as tempfile:
    for each in tempfile.readlines():
        each = each.split(",")
        if (int(each[0]) >= int(startw)) and (int(each[0]) <= int(endw)):
            each = [int(i) for i in each]
            each = each[1:8] 
            temp.append(each)
total = sum(sum(temp, []))
avg = total/((int(endw)-int(startw)+1)*7)
print(total,avg)            