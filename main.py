import csv
import os
from datetime import datetime

FILE_NAME = "patients.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Patient ID",
            "Name",
            "Age",
            "Gender",
            "Blood Group",
            "Disease",
            "Doctor",
            "Phone",
            "Address",
            "Admission Date"
        ])

# Generate Patient ID
def generate_patient_id():
    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))
    return f"P{len(reader):03d}"

# Add Patient
def add_patient():
    patient_id = generate_patient_id()

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    blood = input("Enter Blood Group: ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            patient_id,
            name,
            age,
            gender,
            blood,
            disease,
            doctor,
            phone,
            address,
            date
        ])

    print("\nPatient Added Successfully!")
    print("Patient ID :", patient_id)

# View Patients
def view_patients():
    print("\n---------------- Patient Records ----------------")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

# Search Patient
def search_patient():
    pid = input("Enter Patient ID : ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        found = False

        for row in reader:
            if len(row) > 0 and row[0] == pid:
                print("\nPatient Details")
                print("----------------------------")
                print("Patient ID :", row[0])
                print("Name :", row[1])
                print("Age :", row[2])
                print("Gender :", row[3])
                print("Blood Group :", row[4])
                print("Disease :", row[5])
                print("Doctor :", row[6])
                print("Phone :", row[7])
                print("Address :", row[8])
                print("Admission Date :", row[9])

                found = True
                break

        if not found:
            print("Patient Not Found.")

# Update Patient
def update_patient():
    pid = input("Enter Patient ID : ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and row[0] == pid:

                print("Enter New Details")

                row[1] = input("Name : ")
                row[2] = input("Age : ")
                row[3] = input("Gender : ")
                row[4] = input("Blood Group : ")
                row[5] = input("Disease : ")
                row[6] = input("Doctor : ")
                row[7] = input("Phone : ")
                row[8] = input("Address : ")

                found = True

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Patient Updated Successfully.")

    else:
        print("Patient Not Found.")

# Delete Patient
def delete_patient():

    pid = input("Enter Patient ID : ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and row[0] != pid:
                rows.append(row)
            else:
                if len(row) > 0:
                    found = True

    if found:

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Patient Deleted Successfully.")

    else:
        print("Patient Not Found.")

# Count Patients
def total_patients():

    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    print("\nTotal Patients :", len(reader) - 1)

# Menu
while True:

    print("\n===================================")
    print(" AUTOMATIC PATIENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Total Patients")
    print("7. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        update_patient()

    elif choice == "5":
        delete_patient()

    elif choice == "6":
        total_patients()

    elif choice == "7":
        print("\nThank You...")
        break

    else:
        print("Invalid Choice!")