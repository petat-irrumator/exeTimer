import os
import time

# HERE THE RECENTLY OPENED FILENAME AND TIME WILL BE WRITTEN TO old_record.txt


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


file_dir = input("Directory of the application to run: ")

start_time = int(time.time())

# r is here to get the raw string and ignore the escape characters
os.system(rf'"{file_dir}"')

# getting the seconds for which the file ran and printing it the format hrs,min,sec
end_time = int(time.time())

interval_time = end_time-start_time


input_seconds = time_formatter(interval_time)

print(
    f"Current time this application ran for: {input_seconds[0]} Hours {input_seconds[1]} Minutes {input_seconds[2]} Seconds")


# storing the time and the file name in a txt file
old_record_file = open("old_record.txt ", "a")

record_to_store = rf"{file_dir} was open for {input_seconds[0]} Hours {input_seconds[1]} Minutes {input_seconds[2]} Seconds"

old_record_file.writelines(f"{record_to_store}\n")

old_record_file.close()


# by this point time and file name is written to old_record_file
