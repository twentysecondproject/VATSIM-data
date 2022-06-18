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
    zhu = requests.get(f'https://api.zhuartcc.org/api/users/{CID}').json()
    zhu_cert_list = ["No Certification", "Minor Certification", "Major Certification", "Solo Certification"]
    name = usa['data']['fname']
    lname = usa['data']['lname']
    del_cert = zhu['del_cert']
    gnd_cert = zhu['gnd_cert']
    twr_cert = zhu['twr_cert']
    app_cert = zhu['app_cert']
    ctr_cert = zhu['ctr_cert']
    ocn_cert = zhu['ocn_cert']

    print(f"{name} {lname} ({CID}) has a rating of {rating_list[rat]}")
    print(f'Region: {reg}')
    print(f'Division: {div}')
    facility = usa['data']['facility']
    if division != "BRZ" and division != "CAM" and division != "GBR" and division != "IL" and division != "JPN" and division != "KOR" and division != "PAC" and division != "PRC" and division != "MCO" and division != "NZ" and division != "ROC" and division != "RUS" and division != "USA" and division != "SSA":
        print(f'Subdivision: {sub}')
    elif facility == 'ZHU':
        print(f'Subdivision: {facility}')
        print(f'DEL Cert: {zhu_cert_list[del_cert]}')
        print(f'GND Cert: {zhu_cert_list[gnd_cert]}')
        print(f'TWR Cert: {zhu_cert_list[twr_cert]}')
        print(f'APP Cert: {zhu_cert_list[app_cert]}')
        print(f'CTR Cert: {zhu_cert_list[ctr_cert]}')
        print(f'OCN Cert: {zhu_cert_list[ocn_cert]}')
    elif division == "USA":
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
