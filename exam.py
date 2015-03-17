###########################################
# Changes To This File Will Be Ignored.
###########################################
#
# PART 1
# ------------
# (15 pts) Answer all of the true/false questions:
import exam_true_false

# The following assertion ensures you've answered each question,
# but it does NOT check for correctness.
assert None not in exam_true_false.answers.values(), "You forgot to answer at least one of the multiple choice questions"


# PART 2
# ------------
# Given: flight_data.csv containing a daily flight schedule.
#
# File format is:
#
# Flight Number,Plane Identifier,Origin,Destination,Miles,Passengers
#

from flight_schedule import FlightSchedule
daily_schedule = FlightSchedule()
daily_schedule.read_data_from_file()

# Write code that can answer the following questions.

# 1. (5 pts) How many flights are there in one day?
assert 241 == len(daily_schedule.flights)

# 2. (5 pts) How many different airplanes are flown each?
assert 101 == len(daily_schedule.plane_identifiers)

# 3. (5 pts) Which flight is the longest?
assert 142 == int(daily_schedule.determine_longest_flight())


### HINTS:
### -------
### "Use Error-Driven Development" until all assertions pass.
###
### 1. Before starting to code, run this file and read the error message.
### 2. Do the "Simplest Thing That Can Possibly Work" to resolve the error.
### 3. Run the file again. Repeat until no errors remain.

### You can read rows of data with proper UTF-8 encoding like this:
###
###       with open("myfilename", encoding='utf-8') as file:
###           reader = csv.reader(file)
###               for row in reader:
###
###                  etc.










print("All assertions pass.")
print()
print("IMPORTANT: Commit and sync your code!")
print()
print("Enjoy your spring break!")
print()





