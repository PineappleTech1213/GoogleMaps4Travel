import spacy
import gspread
import google
from google.oauth2.service_account import Credentials

# Load the article into spaCy and identify locations
nlp = spacy.load("en_core_web_sm")
article = "I flew to London from Pittsburgh and then took an early flight to Edinburgh where I arrived at about 11a.m.. After that, it is time for lunch, so I went to the Royal Mile."
doc = nlp(article)
locations = []
for ent in doc.ents:
    print(ent)
    if ent.label_ == "LOC":
        locations.append(ent.text)

print(locations)


# # Authenticate with the Google Sheets API
# scope = ["https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name("gsheetwriter-378419-d50229d7ebf2.json", scope)
# client = gspread.authorize(creds)

# # Create a new sheet in the spreadsheet and write the data
# sheet_name = "Locations"
# spreadsheet = client.create("My Travel Plan")
# worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=len(locations), cols=1)
# for i, loc in enumerate(locations):
#     worksheet.update_cell(i+1, 1, loc)
