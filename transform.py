import json
# This defition allows us to traverse down the json groups finding all children of pe inf and to remove them
def removesubgroups(data,id):
    groups = list(filter(lambda x:x ["parent"]==id,data))
    for group in groups:
        subid = group["id"]
        data = list(filter(lambda x:x ["id"]!=subid,data))
        data = removesubgroups(data,subid)
    return data

# This defintion allows us to traverse down the pe inf tree and find all groups
def addsubgroups(data,id,peinf):
    groups = list(filter(lambda x:x ["parent"]==id,data))
    peinf = peinf + groups
    for group in groups:
        subid = group["id"]
        peinf = addsubgroups(data,subid,peinf)
    return peinf

# open the backup classifiction
with open('classification.json') as data_file:
    data = json.load(data_file)
# open the DR server classification
with open('classificationDR.json') as data_fileDR:
    data_DR = json.load(data_fileDR)

# find the infrastructure group and its ID
peinf = list(filter(lambda x:x ["name"]=="PE Infrastructure",data))
id = peinf[0]["id"]
# remove this group from the list and recursively remove all sub groups
data = list(filter(lambda x:x ["id"]!=id,data))
data = removesubgroups(data,id)

# find the dr ingrastrucutre group and its ID
peinf_DR = list(filter(lambda x:x ["name"]=="PE Infrastructure",data_DR))
id_DR = peinf_DR[0]["id"]
# Recursively go through inf groups to get the full tree
peinf_DR = addsubgroups(data_DR,id_DR,peinf_DR)

# Add the contents of the backup classification without pe inf to the DR pe inf groups
# and write to a file
peinf_transformed_groups = data + peinf_DR
with open('classification_transformed.json', 'w') as fp:
    json.dump(peinf_transformed_groups, fp)
