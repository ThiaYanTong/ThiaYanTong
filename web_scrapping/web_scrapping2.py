with open("text2.txt") as f:
    my_list = f.read().split("</tr>")

course_index = []
date = []
starttime = []
endtime = []
counter = 0

course_index_lec = []
date_lec = []
starttime_lec = []
endtime_lec = []


for each in my_list:

    each_each = each.split('<td>')
    print(each_each)
    for each2 in range(len(each_each)):

        if each2 == 0:
            continue
        if counter % 2 == 0:
            if each2 == 1:
                course_index.append(each_each[each2][3:8])
            if each2 == 4:
                date.append(each_each[each2][3:6].title())
            if each2 == 5:
                starttime.append(each_each[each2][3:7])
                endtime.append(each_each[each2][8:12])
        elif counter % 2 != 0:
            if each2 == 1:
                course_index_lec.append(each_each[each2][3:8])
            if each2 == 4:
                date_lec.append(each_each[each2][3:6].title())
            if each2 == 5:
                starttime_lec.append(each_each[each2][3:7])
                endtime_lec.append(each_each[each2][8:12])
    counter += 1


print(course_index)
print(date)
print(starttime)
print(endtime)

print(course_index_lec)
print(date_lec)
print(starttime_lec)
print(endtime_lec)



print(len(course_index))
print(len(date))
print(len(starttime))
print(len(endtime))

code = 'HE5091'
name = 'PRINCIPLES OF ECONOMICS'

with open(f"{code}.txt","w") as f_w:
    for each in range(len(course_index)):
        f_w.write(f'INSERT into courses (code, name, course_index, date, start_time, end_time) VALUES ("{code}","{name}","{course_index_lec[each]}","{date[each]}","{starttime[each]}","{endtime[each]}");\n')
    f_w.write(f'INSERT into courses (code, name, course_index, date, start_time, end_time) VALUES ("{code + "-L"}","{name + " LEC"}","{code + "-L"}","{date_lec[0]}","{starttime_lec[0]}","{endtime_lec[0]}");\n')
# INSERT INTO table_name (column1, column2, column3, ...)
# VALUES (value1, value2, value3, ...);
