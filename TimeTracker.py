import datetime
import csv

# datetime(year, month, day, hour, minute, second) - initialise

start_time = None
activity = None


def read_csv(filename):
    with open(filename, mode="r+") as csv_file:
        rows = [row for row in csv.reader(csv_file)]
    return rows


def seconds_to_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 3600) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"  # f strings, :02d - fills in


def time_to_seconds(time_string):
    hours = int(time_string.split(":")[0])
    minutes = int(time_string.split(":")[1])
    seconds = int(time_string.split(":")[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def start(area):
    global start_time  # references global variable
    global activity

    if activity is None:
        activity = area
        now = datetime.now()
        print("Starting " + area + ": " + now.strftime("%d/%m/%Y %H:%M:%S"))
        start_time = now
    elif activity == area:
        print(f"{activity} has already started.")
    else:
        print(f"{activity} in progress.")


def end(area):
    global start_time
    global activity

    if activity == area:
        now = datetime.now()
        print("Ending " + area + ": " + now.strftime("%d/%m/%Y %H:%M:%S"))

        elapsed = now - start_time
        elapsed = round(elapsed.total_seconds())

        print(f"Time elapsed = {seconds_to_time(elapsed)}")
        activity = None

        return elapsed

    elif activity != area:
        print(f"{activity} has not started yet")


# TODO: implement manual override (in order to add activities not using the PC)


# TODO: write to file
# no row with date, add date
# if no col with area, add area
# if date == row, if area == col: add time - in hour/min/seconds format


# TODO: create input loop


# TODO: test cases
def test_case1():
    start("Pharmacy")
    start("Gym")
    start("Pharmacy")
    end("Gym")
    end("Pharmacy")


test_case1()
