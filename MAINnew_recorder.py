from collections import defaultdict
from numpy import source
import old_recorder
# This script takes the entries from old_record.txt and then puts them into new_record.txt

# txt file where the script will store the final result
output_file = open(
    r"D:\All-vs-studio-vs-code-sublimeProjects\VS-Code-Projects\exeTimer\new_record.txt", "w")


def to_seconds(hours, minutes, seconds):
    # this function converts HRS,MIN,SEC to seconds
    hrs_sec = int(hours*3600)
    min_sec = int(minutes*60)

    total_sec = hrs_sec+min_sec+int(seconds)
    return total_sec


def time_formatter(input_seconds):
    # this function converts the input_seconds into the format hour,min,sec

    hours = float(input_seconds/3600)
    # getting the decimal part of the float hours
    decimal_hours = hours - int(hours)

    minutes = float(decimal_hours*60)
    # getting the decimal part of the float minutes
    decimal_minutes = minutes-int(minutes)

    seconds = int(decimal_minutes*60)

    # returning only the int part in the format hr,min,sec
    return int(hours), int(minutes), seconds


# opening the old_record.txt file reading its entries line by line, storing them in a list ()
old_record_file = open(
    r"D:\All-vs-studio-vs-code-sublimeProjects\VS-Code-Projects\exeTimer\old_record.txt", "r")


entries_with_escape_char = old_record_file.readlines()
clean_entries = []
exe_names = []

# removing the escape char \n from every entry of the list entries_with_escape_char and storing those clean strings in a list called clean_entries"

for entry in entries_with_escape_char:

    s = entry
    escapes = ''.join([chr(char) for char in range(1, 32)])
    translator = str.maketrans('', '', escapes)
    t = s.translate(translator)

    clean_entries.append(t)


# print(entries_with_escape_char)
# print(clean_entries)

# putting the exe names in a list
for entry in clean_entries:

    was_index = entry.find("was")
    exe_name = entry[:was_index]

    exe_names.append(exe_name)


# print(exe_names)

# getting the indexes of the exe names which are equal

source = exe_names


def list_duplicates(seq):
    tally = defaultdict(list)

    for i, item in enumerate(seq):
        tally[item].append(i)
    return ((key, locs) for key, locs in tally.items()
            if len(locs) > 1)


# getting every time associated with each duplicate exe name
exe_occurrence_list = sorted(list_duplicates(source))


for tuple in exe_occurrence_list:
    index_list = tuple[1]
    # print(index_list)
    duplicate_exe_list = []
    duplicate_hours_list = []
    duplicate_minutes_list = []
    duplicate_seconds_list = []

    for index in index_list:
        exe_with_time = clean_entries[index]
        duplicate_exe_list.append(exe_with_time)

    # adding the every time associated with each duplicate exe name
    for exe in duplicate_exe_list:
        for_index = exe.find("for")+3
        hour_index = exe.find("Hours")
        minutes_index = exe.find("Minutes")
        seconds_index = exe.find("Seconds")

        duplicate_hours = int(exe[for_index:hour_index])
        duplicate_minutes = int(exe[hour_index+5:minutes_index])
        duplicate_seconds = int(exe[minutes_index+7:seconds_index])

        duplicate_hours_list.append(duplicate_hours)
        duplicate_minutes_list.append(duplicate_minutes)
        duplicate_seconds_list.append(duplicate_seconds)

    #print(duplicate_hours_list, duplicate_minutes_list, duplicate_seconds_list)

    # getting the sum of every time associated with each duplicate exe name

    total_hours = 0
    total_minutes = 0
    total_seconds = 0

    for hours in duplicate_hours_list:
        total_hours += hours

    for minutes in duplicate_minutes_list:
        total_minutes += minutes

    for seconds in duplicate_seconds_list:
        total_seconds += seconds

    #print(total_hours, total_minutes, total_seconds)

    seconds = to_seconds(total_hours, total_minutes, total_seconds)

    hr_min_sec_format = time_formatter(seconds)

    # print(seconds)
    #print(tuple[0], hr_min_sec_format)
    # storing the time and exe name to a txt file

    output_str = f"{tuple[0]} was open for {hr_min_sec_format[0]} Hours {hr_min_sec_format[1]} Minutes {hr_min_sec_format[2]} Seconds"

    output_file.write(f"{output_str}\n")

    # print(output_str)

output_file.close()

old_record_file.close()

print("Total Time can be viewed from the file new_record.txt")
print("Note: The time only registers in new_record.txt if you have run the executable at least twice")
