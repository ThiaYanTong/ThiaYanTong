with open("/workspaces/117797018/web_scrapping/text2.txt") as f:
    my_list = f.read().split("</tr>")

course_index = []
date = []
starttime = []
endtime = []
for each in my_list:

    each_each = each.split('<td>')

    for each2 in range(len(each_each)):
        if each2 == 0:
            continue
        if each2 == 1:
            course_index.append(each_each[each2][3:8])
        if each2 == 4:
            date.append(each_each[each2][3:6].title())
        if each2 == 5:
            starttime.append(each_each[each2][3:7])
            endtime.append(each_each[each2][8:12])


print(course_index)
print(date)
print(starttime)
print(endtime)

print(len(course_index))
print(len(date))
print(len(starttime))
print(len(endtime))
code = 'AB1201'
name = 'FINANCIAL MANAGEMENT'

with open(f"{code}.txt","w") as f_w:
    for each in range(len(course_index)):
        f_w.write(f'INSERT into courses (code, name, course_index, date, start_time, end_time) VALUES ("{code}","{name.title()}","{course_index[each]}","{date[each]}","{starttime[each]}","{endtime[each]}");\n')

# INSERT INTO table_name (column1, column2, column3, ...)
# VALUES (value1, value2, value3, ...);
