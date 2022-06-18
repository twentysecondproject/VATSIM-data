import requests

CID = input()
x = requests.get(f'https://api.vatsim.net/api/ratings/{CID}').json()
y = requests.get(f'https://api.vatsim.net/api/ratings/{CID}/rating_times/').json()

cid = CID
rating_list = ["Unknown", "OBS", "S1", "S2", "S3", "C1", "C2", "C3", "I1", "I2", "I3", "SUP", "ADM"]
rat = x['rating']
region = x['region']
division = x['division']
subdivision = x['subdivision']
s1 = y['s1']
s2 = y['s2']
s3 = y['s3']
c1 = y['c1']
c2 = y['c2']
c3 = y['c3']
i1 = y['i1']
i2 = y['i2']
i3 = y['i3']
sup = y['sup']
adm = y['adm']
atc = y['atc']


if division != "BRZ" and division != "CAM" and division != "GBR" and division != "IL" and division != "JPN" and division != "KOR" and division != "PAC" and division != "PRC" and division != "MCO" and division != "NZ" and division != "ROC" and division != "RUS" and division != "USA" and division != "SSA":
    a = requests.get(f'https://api.vatsim.net/api/subdivisions/{subdivision}/').json()
    sub = a['fullname']


b = requests.get(f'https://api.vatsim.net/api/divisions/{division}/').json()
c = requests.get(f'https://api.vatsim.net/api/regions/{region}/').json()
div = b['name']
reg = c['name']

try:
    usa = requests.get(f'https://api.vatusa.net/v2/user/{CID}').json()
    name = usa['data']['fname']
    lname = usa['data']['lname']

    print(f"{name} {lname} ({CID}) has a rating of {rating_list[rat]}")
    print(f'Region: {reg}')
    print(f'Division: {div}')
    if division != "BRZ" and division != "CAM" and division != "GBR" and division != "IL" and division != "JPN" and division != "KOR" and division != "PAC" and division != "PRC" and division != "MCO" and division != "NZ" and division != "ROC" and division != "RUS" and division != "USA" and division != "SSA":
        print(f'Subdivision: {sub}')
    elif division == "USA":
        facility = usa['data']['facility']
        print(f'Subdivision: {facility}')
    else:
        print('Subdivision: None')
    print(f'ATC: {atc}')
    print(f'S1: {s1}')
    print(f'S2: {s2}')
    print(f'S3: {s3}')
    print(f'C1: {c1}')
    print(f'C2: {c2}')
    print(f'C3: {c3}')
    print(f'I1: {i1}')
    print(f'I2: {i2}')
    print(f'I3: {i3}')
    print(f'SUP: {sup}')
    print(f'ADM: {adm}')

except:

    print(f"{cid} has a rating of {rating_list[rat]}")
    print(f'Region: {reg}')
    print(f'Division: {div}')
    if division != "BRZ" and division != "CAM" and division != "GBR" and division != "IL" and division != "JPN" and division != "KOR" and division != "PAC" and division != "PRC" and division != "MCO" and division != "NZ" and division != "ROC" and division != "RUS" and division != "USA" and division != "SSA":
        print(f'Subdivision: {sub}')
    else:
        print('Subdivision: None')
    print(f'ATC: {atc}')
    print(f'S1: {s1}')
    print(f'S2: {s2}')
    print(f'S3: {s3}')
    print(f'C1: {c1}')
    print(f'C2: {c2}')
    print(f'C3: {c3}')
    print(f'I1: {i1}')
    print(f'I2: {i2}')
    print(f'I3: {i3}')
    print(f'SUP: {sup}')
    print(f'ADM: {adm}')
