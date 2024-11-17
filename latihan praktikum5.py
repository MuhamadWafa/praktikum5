# List to store student data
data_list = []

# Function to calculate final grade
def calculate_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

# Loop to collect data
while True:
    # Get student data
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS : "))
    uas = float(input("Nilai UAS : "))

    # Calculate final grade
    final_grade = calculate_final_grade(tugas, uts, uas)

    # Store data in a dictionary and add to list
    student_data = {
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": final_grade
    }
    data_list.append(student_data)

    # Ask if the user wants to add more data
    more_data = input("Tambah data(y/t)? ")
    if more_data.lower() != 'y':
        break

# Display all data in a table format
print("\n| No |    Nama    |  NIM  | Tugas | UTS | UAS |  Akhir  |")
print("=" * 55)
for idx, student in enumerate(data_list, start=1):
    print(f"| {idx:<2} | {student['Nama']:<10} | {student['NIM']:<5} | "
          f"{student['Tugas']:<5} | {student['UTS']:<3} | {student['UAS']:<3} | "
          f"{student['Nilai Akhir']:<7.2f} |")