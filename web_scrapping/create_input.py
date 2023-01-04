courses = ['AB1202','AB1301','AB1501',"AB1601","HE5091"]

# for course in courses:
#     with open(f"{course}.txt") as f:
#         with open("input.txt","a") as fw:
#             fw.write(f.read())

# with open() as f:
#     for each in f.readlines():
#         print(each)

str = 'UPDATE courses set course_index_value = (select course_index from courses WHERE id = 2) WHERE id = 2;'
with open("test.txt","w") as fw:
    for each in range(103):
        fw.write(f"UPDATE courses set course_index_value = (select course_index from courses WHERE id = {each}) WHERE id = {each};\n")