#def get_odd_index_elements(input_lists):
#    odd_index_elements = []

#    for lst in input_lists:
#        odd_index_elements.append(lst[1::2])

#    return odd_index_elements


#list_1 = [0, 1, 2, 3, 4, 5]
#list_2 = ['Matt', 'Andy', 'Tom', 'Jeremy']
#items = [list_1, list_2]

#odd_index_elements = get_odd_index_elements(items)
#print(odd_index_elements)



#from datetime import datetime
#import time

#def day_of_the_week(dt):
#    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#    day_index = dt.weekday()
#    return weekdays[day_index]


#example_dt1 = datetime(2019, 9, 6, 11, 33, 0)
#example_dt2 = datetime(2000, 12, 25, 12, 0, 0)

#print(day_of_the_week(example_dt1))
#print(day_of_the_week(example_dt2))



import os

def traversal_count(path):
    file_count = 0

    for entry in os.scandir(path):
        if entry.is_file():
            file_count += 1

    return file_count


print(traversal_count('/opt/yarn/bin/'))
print(traversal_count('/usr/share/X11/'))