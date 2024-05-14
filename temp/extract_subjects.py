from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('../raw-data/Faculty of Liberal Arts and Professional Studies - (AP).html', 'r') as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the select tag and extract options
select_tag = soup.find('select')
# options = select_tag.find_all('option')
# values = [option.get('value') for option in options]
# Extract text from each option and print
options_text = [option.text.strip() for option in select_tag.find_all('option')]
print("Extracted values:")

# Values for faculty_abbrev and faculty
faculty_abbrev = "AP"
faculty = "Faculty of Liberal Arts and Professional Studies"

# Loop through options_text and modify each entry
modified_options_text = []
for option_text in options_text:
    
    # Strip leading and trailing spaces from the option text
    option_text = option_text.strip()

    # Split the text by ' - ' and extract the abbreviation and full name
    abbreviation, full_name = option_text.split(' - ', 1)
    
    # Remove trailing spaces from the abbreviation
    abbreviation = abbreviation.rstrip()
    
    # Create the modified text
    modified_text = f"{faculty},{faculty_abbrev},{abbreviation},{full_name}"
    
    # Append the modified text to the list
    modified_options_text.append(modified_text)

# Print the modified options
for modified_text in modified_options_text:
    print(modified_text)


# # Write the extracted values to a CSV file
# with open('output.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Value'])
#     for value in values:
#         writer.writerow([value])

# print("Values written to output.csv")
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