import os
import current_file_recorder

# THIS SCRIPT TAKES THE OLD RECORD FILE ,DETECTS THE LINES HAVING THE SAME FILE NAME ,TAKE THE TIME OF EACH LINE SUMS IT, CONVERTS THE TAKEN TIME TO SECONDS (SINCE IT CAN BE IN INVALID FORMAT LIKE:3HR,70MIN,30SEC),THEN PASS THE TOTAL SECONDS TO FUNCTION (time_formatter) IN THE SCRIPT main.py


def old_record_file_time_adder(input_file, current_open_file):
    # this function takes the filename (var current_open_file) checks if the input_file already contain files with the same file name IF it does then adds the hours, min and sec of each occurence (this yeilds TIME IN INVALID FORMAT)

    function_old_record_file = open(input_file, "r")

    old_data = function_old_record_file.readlines()

    hours_list = []
    minutes_list = []
    seconds_list = []

    occurrence = 0

    for file in old_data:

        # if this value is not -1 then the current_open_file is in old_record_file
        name_status = file.find(current_open_file)

        if name_status != -1:

            occurrence += 1

            print(f"{current_open_file} is found in {input_file}")

            # getting the hours for each file name (which is var file)

            for_index = file.find("for")
            hours_index = file.find("Hours")

            start_index = for_index+3
            end_index = hours_index-1

            hours_list.append(int(file[start_index:end_index]))

            # getting the minutes for each file name (which is var file)

            hours_index = file.find("Hours")
            minutes_index = file.find("Minutes")

            start_index = hours_index+5
            end_index = minutes_index-1

            minutes_list.append(int(file[start_index:end_index]))

            # getting the seconds for each file name (which is var file)

            minutes_index = file.find("Minutes")
            seconds_index = file.find("Seconds")

            start_index = minutes_index+7
            end_index = seconds_index-1

            seconds_list.append(int(file[start_index:end_index]))

    # adding all the elements of hrs,min and sec list to get the total time
    total_hours = 0
    total_minutes = 0
    total_seconds = 0

    for hour in hours_list:
        total_hours += hour

    for minute in minutes_list:
        total_minutes += minute

    for second in seconds_list:
        total_seconds += second

    function_old_record_file.close()
    print(f"{occurrence} occurrences are found ")

    return total_hours, total_minutes, total_seconds


invalid_time_data = old_record_file_time_adder(
    "old_record.txt", rf"{current_file_recorder.file_dir}")


# print(invalid_time_data)

# converting invalid time (like 3hr70min10sec) to seconds then feeding it to time_formatter
valid_total_seconds = (invalid_time_data[0]*3600) + \
    (invalid_time_data[1]*60)+invalid_time_data[2]

valid_time_data = current_file_recorder.time_formatter(valid_total_seconds)


print(
    f"Total time that you ran this application is : {valid_time_data[0]} Hour {valid_time_data[1]} Minute {valid_time_data[2]} Second")
