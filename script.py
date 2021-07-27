# List of names
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]

# List of insurance cost
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
# Append a new individual (Priscilla) to the list of names
names.append("Priscilla")

# Append a new value to the list of insurance_cost
insurance_costs.append(8320.0)

# Combine insurance_costs and names by setting it to a new variable (medical_records) using the zip() function
medical_records = list(zip(insurance_costs, names))

# Display medical records
print(medical_records)

# Assign the length of medical_records to num_medical_records
num_medical_records = len(medical_records)

# Display num_medical_records in an informative way

print("\nThere are " + str(num_medical_records) + " " + "medical records.")

# Select the first medical record in medical_records, and save it to  first_medical_record
first_medical_record = medical_records[0]

# Display first_medical_record
print("\nHere is the first medical record: " + str(first_medical_record))

# Sort medical_records
medical_records.sort()

# Display the sorted medical_records
print("\nHere are the medical records sorted by insurance costs: " + str(medical_records))

# Store the three cheapest insurance costs in cheapest_three
cheapest_three = medical_records[:3]

# Display cheapest_three
print("\nHere are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Store the three most expensive insurance costs in priciest_three
priciest_three = medical_records[-3:]

# Display priciest_three
print("\nHere are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# Count the number of time "Paul" appear in names and setting it to occurrences_paul
occurrences_paul = names.count("Paul")

# Display occurrences_paul
print("\nThere are " + str(occurrences_paul) + " " + "individuals with the name Paul in our medical records.")

# Display a new line
print("\n")

# Sort the medical records alphabetically by name and setting it to medical_records_sort
medical_records_sort = list(zip(names, insurance_costs))

# Display medical_records_sort
print(medical_records_sort)

# Select the medical records starting at index 3 and ending at index 7 and save it in a variable called middle_five_records
middle_five_records = medical_records_sort[3:8]

# Display middle_five_records
print("\n" + str(middle_five_records))