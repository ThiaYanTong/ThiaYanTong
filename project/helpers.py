from cs50 import SQL
import pandas as pd
import itertools
db = SQL("sqlite:///courses_actual.db")
columns = ["Mon","Tue","Wed","Thu","Fri","Sat"]
indexs = ["0730","0830","0930","1030","1130","1230","1330","1430","1530","1630","1730","1830","1930","2030","2130","2230"]



def checker(end_time):
    if len(str(int(end_time)-100)) == 3:
        return "0"+str(int(end_time)-100+10)
    return str(int(end_time)-100+10)

def create_s():
    tmp = []
    s = []
    for each in range(6):
        for each in range(16):
            tmp.append("0")
        s.append(tmp)
        tmp = []
    return s


def logic(comb):
    s = create_s()
    for course_index_info in comb:

        date_index = columns.index(course_index_info['date'])
        start_splicing_index = (int((lambda x: (x - 730)/100)(int(course_index_info['start_time']))))
        end_splicing_index = (int((lambda x: (x + 10 - 730)/100)(int(course_index_info['end_time']))))


        if '1' in s[date_index][start_splicing_index:end_splicing_index]:
            return False
        else:
            s[date_index][start_splicing_index:end_splicing_index] = list(map(lambda x: x.replace("0", "1"), s[date_index][start_splicing_index:end_splicing_index]))

    s = None
    s = create_s()
    return True


def process(requested):
    index_info = []

    for each_request in requested:

        course_indexs_data = db.execute("select code,name,course_index,date,start_time,end_time from courses where code = ?",each_request)
        index_info.append(course_indexs_data)

    combs = itertools.product(*index_info)

    filtered_combs = (prod for prod in combs if logic(prod) == True)

    return list(filtered_combs)


def plot(filtered_list,index):

    comb = filtered_list[index]
    df = pd.DataFrame(columns = columns, index = indexs)

    for each_index in comb:
        df.loc[each_index['start_time']:checker(each_index['end_time']),each_index['date']] = each_index['code']
    return df