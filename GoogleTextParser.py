# Imports the Google Cloud client library
from google.cloud import language_v1
#import service account credentials
from google.oauth2 import service_account

# Instantiates a client
#provide credentials

credentials = service_account.Credentials.from_service_account_file("gsheetwriter-378419-d50229d7ebf2.json")
client = language_v1.LanguageServiceClient(credentials=credentials)

# The text to analyze
text = "I flew to London from Pittsburgh and then took an early flight to Edinburgh where I arrived at about 11a.m.. After that, it is time for lunch, so I went to the Royal Mile."
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# parse the entities in the text
entities = client.analyze_entities(request={'document': document}).entities

#find out location entities and put them in a list
location_entities = []
for entity in entities:
    if entity.type_ == language_v1.Entity.Type.LOCATION:
        location_entities.append(entity.name)

#find out the transportation entities and put them in a list
transportation_entities = []
for entity in entities:
    if entity.type_ == language_v1.Entity.Type.EVENT:
        transportation_entities.append(entity.name)


#print the list
print(location_entities)
print(transportation_entities)


#print out all entities and their type names
for entity in entities:
    print(u"Representative name for the entity: {}".format(entity.name))
    print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_)))


#get the google maps coordinates for the locations

