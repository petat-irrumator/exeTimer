import os
import old_record_time_manager

# THIS SCRIPT CREATES A LOG FILE (new_record.txt) THAT CONTAINS THE FILENAME WITH THE TOTAL TIME THEY ARE RAN

# first checking if new_record.txt even exists in the current directory IF not then creating it

current_dir_contents = os.listdir()

for dir in current_dir_contents:

    if dir == "new_record.txt":
        pass  # new_record.txt is present
    else:
        new_record_file = open("new_record.txt", "a")
        new_record_file.close()


def new_record_file_same_line_checker_new_list_maker(exe_name, time):
    # this function will take the executable name(the exe that you wanted to record the time of) , and the time it was open (total time as a tuple )checks if new_record.txt already has a line with the same filename if yes then makes a new list where those duplicate items are not present and then append this new list with the provided exe name and time
    function_new_record_file = open("new_record.txt", "r")

    newest_data_to_append = f"{exe_name} was open for {time[0]} Hours {time[1]} Minutes {time[2]} Seconds"

    new_record_file_data_new_list = []  # this is the new list where the good data is
    new_record_file_data_duplicate_list = []

    new_record_file_data_old_list = function_new_record_file.readlines()

    # detecting duplicates and making a new list where the duplicates are not found
    for file_name in new_record_file_data_old_list:

        # if this is not -1 that means exe_name is already present in function_new_record_file
        duplicate_file_name_checker = file_name.find(exe_name)

        if duplicate_file_name_checker != -1:

            new_record_file_data_duplicate_list.append(file_name)

        elif duplicate_file_name_checker == -1:

            new_record_file_data_new_list.append(file_name)

    new_record_file_data_new_list.append(f"{newest_data_to_append}")

    function_new_record_file.close()

    return new_record_file_data_new_list


new_data_list = new_record_file_same_line_checker_new_list_maker(
    rf"{old_record_time_manager.current_file_recorder.file_dir}", old_record_time_manager.valid_time_data)  # (remember (hour,min,sec))

# print(new_data_list)

# writing the new_data_list to the new_record.txt file
new_record_file = open("new_record.txt", "w")

# HERE DONT PUT FORMATTED STRING
new_record_file.writelines(new_data_list)

new_record_file.close()

print("Full logs can be viewed in new_records.txt")

# VOILA
