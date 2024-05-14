from bs4 import BeautifulSoup
import csv
import os
from datetime import date, datetime

# Read courses_subjects.csv and create a dictionary mapping course values to subjects
subjects_dict = {}
with open('course_subjects.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        subjects_dict[row[0]] = row[1]

# Read courses_faculties.csv and create a dictionary mapping course values to faculties
faculties_dict = {}
with open('course_faculties.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        faculties_dict[row[0]] = row[1]

# Initialize CSV string
csv_data = ""
year = ""
count = 0
# Loop through HTML files in the by_campus folder
for filename in os.listdir('./raw-data/by_campus/2024_2025'):
    if filename.endswith('.html'):
        print("Reading: ", filename)
        # Read the HTML file
        with open(os.path.join('./raw-data/by_campus/2024_2025', filename), 'r') as file:
            html = file.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Find all rows in the table
        rows = soup.find_all('tr', bgcolor="#ffffff")

        # Initialize a set to store unique rows
        unique_rows = set()

        # Loop through each row and extract course and title
        for row in rows:
            # Extract course and title
            course_raw = row.find('td').text.strip().split()[0]  # Extract 'GS/VISA'
            faculty_abbrev, subject_abbrev = course_raw.split('/', 1)
            title = row.find_all('td')[1].text.strip()  # Extract title

            # Extract season from the third column
            schedule_text = row.find_all('td')[2].text.strip()
            season = schedule_text.split()[0]  # Extract 'Fall/Winter'

            # Extract years from the third column
            start_year = schedule_text.split()[-3]  # Extract '2023'

            # Extract course schedule URL
            schedule_url = row.find('a')['href']

            # Enrich CSV data with subjects and faculties, if not found sub 'unknown'
            subject = subjects_dict.get(subject_abbrev, "Unknown Subject")
            faculty = faculties_dict.get(faculty_abbrev, "Unknown Faculty")

            # Append to CSV string
            csv_data += f"{season},{start_year},{faculty_abbrev},{faculty},{subject_abbrev},{subject},{title}\n"
            year = start_year
            count = count + 1 

# Write CSV data to a file
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"{year}_courses_output_{formatted_datetime}.csv"
output_path = os.path.join("./output", output_file)
with open(output_path, 'w', newline='') as csvfile:
    csvfile.write("academic_term,academic_year,faculty,faculty_abbrev,subject,subject_abbrev,title\n")
    csvfile.write(csv_data)

# Print CSV data to the screen
print("academic_term,academic_year,faculty,faculty_abbrev,subject,subject_abbrev,title")
print(csv_data)
print("Records", count)

## Reference
# t.string "faculty"
# t.string "faculty_abbrev"
# t.string "subject"
# t.string "subject_abbrev"
# t.string "academic_term"
# t.string "academic_year"
# t.string "year_level"
# t.string "professor"
# t.integer "number"
# t.integer "credits"
# t.string "title"
# t.string "title2"
# t.string "section"