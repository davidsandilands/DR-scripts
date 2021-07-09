import json
# This defition allows us to traverse down the json groups finding all children
def removesubgroups(data,id):
    groups = list(filter(lambda x:x ["parent"]==id,data))
    for group in groups:
        subid = group["id"]
        data = list(filter(lambda x:x ["id"]!=subid,data))
        data = removesubgroups(data,subid)
    return data

# this is just returning one value
def addsubgroups(dataDR,id,peinf):
    groups = list(filter(lambda x:x ["parent"]==id,data))
    peinf = peinf + groups
    for group in groups:
        subid = group["id"]
        peinf = addsubgroups(dataDR,subid,peinf)
    return peinf

# open the backup classifiction
with open('classification.json') as data_file:
    data = json.load(data_file)
# open the DR server classification
with open('classificationDR.json') as data_fileDR:
    data_DR = json.load(data_fileDR)

peinf = list(filter(lambda x:x ["name"]=="PE Infrastructure",data))
id = peinf[0]["id"]
data = removesubgroups(data,id)

peinf_DR = list(filter(lambda x:x ["name"]=="PE Infrastructure",data))
id_DR = peinf_DR[0]["id"]
peinf_groups_DR = addsubgroups(data_DR,id_DR,peinf_DR)
print(peinf_groups_DR)
peinf_transformed_groups = data + peinf_groups_DR
#print(peinf_transformed_groups)


#list(map(lambda x:x if x["id_number"]=="cz1093" ,data)
# remove our item from list
#remove item from data
#done
# find pe inf id
# remove pe inf
# recurse down through children
# for each find id, remove and recurse down
# join this data with DR data
#with open('transformclassification.json', 'w') as f:
#    json.dump(data, f)