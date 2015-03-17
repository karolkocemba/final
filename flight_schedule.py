import csv

class FlightSchedule:

	def __init__(self):
		self.flights = []
		self.plane_identifiers = []
		self.miles = []

	def read_data_from_file(self):
		with open("flight_data.csv", encoding='utf-8') as file:
			reader = csv.reader(file)
			for row in reader:
				self.flights.append(row[0])
				self.miles.append(int(row[4]))
				if row[1] not in self.plane_identifiers:
					self.plane_identifiers.append(row[1])

	def determine_longest_flight(self):
		longest_flight_length = max(self.miles)
		longest_flight_index = self.miles.index(longest_flight_length)
		return self.flights[longest_flight_index]
