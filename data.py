import requests
from datetime import datetime

def ask_for_options():
    print()
    print('1. Get user data')
    print('2. Get metar data')
    print('3. Get controllers at an airport (will return all the stations online at the airport, might not return CTRs')
    print('4. Get callsign data')
    print('5. Exit')
    inpot = input('What do you want to do? (1/2/3/4/5): ')
    if inpot == '1':
        get_user_data()
    elif inpot == '2':
        get_metar_data()
    elif inpot == '3':
        get_controllers()
    elif inpot == '4':
        get_pilot()
    elif inpot == '5':
        exit()
    else:
        print('Invalid input')
        ask_for_options()


def ask_for_exit():
            print()
            inpot = input('Do you want to continue? (y/n): ')
            if inpot == 'y':
                ask_for_options()
            elif inpot == 'n':
                exit()
            else:
                print('Invalid input')
                ask_for_exit()


def get_user_data():
    CID = input('You might want to give me a CID: ')
    code = requests.get(f'https://api.vatsim.net/api/ratings/{CID}')
    codes = code.status_code
    if codes == 404:
        print('CID not found')
        ask_for_exit()

    x = requests.get(f'https://api.vatsim.net/api/ratings/{CID}').json()
    y = requests.get(f'https://api.vatsim.net/api/ratings/{CID}/rating_times/').json()
    cid = CID
    da = x['reg_date']
    dat = datetime.strptime(da, '%Y-%m-%dT%H:%M:%S')
    date = dat.strftime('%d/%m/%Y')
    rating_list = ["Unknown", "OBS", "S1", "S2", "S3", "C1", "C2", "C3", "I1", "I2", "I3", "SUP", "ADM"]
    rat = x['rating']
    region = x['region']
    division = x['division']
    subdiv = x['subdivision']
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
    pilot = y['pilot']
    atc = y['atc']

    if len(subdiv) - subdiv.count(' ') != 0:       
        a = requests.get(f'https://api.vatsim.net/api/subdivisions/{subdiv}').json()
        sub = a['fullname']
    
    b = requests.get(f'https://api.vatsim.net/api/divisions/{division}/').json()
    c = requests.get(f'https://api.vatsim.net/api/regions/{region}/').json()
    div = b['name']
    reg = c['name']



    try:

        usa = requests.get(f'https://api.vatusa.net/v2/user/{CID}').json()
        facility = usa['data']['facility']
        name = usa['data']['fname']
        lname = usa['data']['lname']


        if facility == "ZHU":
            zhu = requests.get(f'https://api.zhuartcc.org/api/users/{CID}').json()
            cert_list = ["No Certification", "Minor Certification", "Major Certification", "Solo Certification"]
            del_cert = zhu['del_cert']
            gnd_cert = zhu['gnd_cert']
            twr_cert = zhu['twr_cert']
            app_cert = zhu['app_cert']
            ctr_cert = zhu['ctr_cert']
            ocn_cert = zhu['ocn_cert']
            print()
            print(f"{name} {lname} ({CID}) has a rating of {rating_list[rat]}")
            print(f'Registartion date (Day/Month/Year): {date}')
            print(f'Region: {reg}')
            print(f'Division: {div}')
            print(f'Facility: Houston ARTCC (ZHU)')
            print(f'DEL Cert: {cert_list[del_cert]}')
            print(f'GND Cert: {cert_list[gnd_cert]}')
            print(f'TWR Cert: {cert_list[twr_cert]}')
            print(f'APP Cert: {cert_list[app_cert]}')
            print(f'CTR Cert: {cert_list[ctr_cert]}')
            print(f'OCN Cert: {cert_list[ocn_cert]}')
            print(f'ATC: {atc}')
            print(f'Pilot: {pilot}')
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
            ask_for_exit()

        elif facility == "ZJX":
                zjx = requests.get(f'https://zjxartcc.org/api/user/{CID}').json()
                cert_list = ["No Certification", "Minor Certification", "Major Certification", "Minor Solo Certification", "Major Solo Certification", 'Checkout Required', 'Training Request Recived', 'Training Request Recived']
                del_cert = zjx['del_cert']
                gnd_cert = zjx['gnd_cert']
                twr_cert = zjx['twr_cert']
                app_cert = zjx['app_cert']
                ctr_cert = zjx['ctr_cert']
                print()
                print(f"{name} {lname} ({CID}) has a rating of {rating_list[rat]}")
                print(f'Registartion date (Day/Month/Year): {date}')
                print(f'Region: {reg}')
                print(f'Division: {div}')
                print(f'Facility: Jacksonville ARTCC (ZJX)')
                print(f'DEL Cert: {cert_list[del_cert]}')
                print(f'GND Cert: {cert_list[gnd_cert]}')
                print(f'TWR Cert: {cert_list[twr_cert]}')
                print(f'APP Cert: {cert_list[app_cert]}')
                print(f'CTR Cert: {cert_list[ctr_cert]}')
                print(f'ATC: {atc}')
                print(f'Pilot: {pilot}')
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
                ask_for_exit()

        else:
                print()
                print(f"{name} {lname} ({CID}) has a rating of {rating_list[rat]}")
                print(f'Registartion date (Day/Month/Year): {date}')
                print(f'Region: {reg}')
                print(f'Division: {div}')
                if division == 'USA':
                    print(f'Facility: {facility}')
                elif len(subdiv) - subdiv.count(' ') == 0:
                    print(f'Subdivision: None')
                else:
                    print(f'Subdivision: {sub}')
                print(f'ATC: {atc}')
                print(f'Pilot: {pilot}')
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
                ask_for_exit()

    except:
        print()
        print(f"{cid} has a rating of {rating_list[rat]}")
        print(f'Registartion date (Day/Month/Year): {date}')
        print(f'Region: {reg}')
        print(f'Division: {div}')
        if len(subdiv) - subdiv.count(' ') == 0:
            print(f'Subdivision: None')
        else:
            print(f'Subdivision: {sub}')
        print(f'ATC: {atc}')
        print(f'Pilot: {pilot}')
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
        ask_for_exit()
        
def get_metar_data():
    print()
    icao = input("Enter ICAO for Metar: ")
    req = requests.get(f"https://metar.vatsim.net/{icao}")
    resp = req.text
    print(resp)
    ask_for_exit()


def get_controllers():
    print()
    icao = input("Enter the ICAO (IATA if in the United States) to get the online controllers: ")
    json = requests.get('https://data.vatsim.net/v3/vatsim-data.json').json()
    controllers = json['controllers']
    for controller in controllers:
        if controller['callsign'][:len(icao)] == icao:
            print(f"{controller['callsign']} - {controller['name']}")
    ask_for_exit()

def get_pilot():
    print()
    callsign = input("Enter the callsign of the pilot: ")
    json = requests.get('https://data.vatsim.net/v3/vatsim-data.json').json()
    pilots = json['pilots']
    for pilot in pilots:
        if pilot['callsign'] == callsign:
            flight_plan = pilot['flight_plan']
            flight_rule =flight_plan['flight_rules']
            route = flight_plan['route']
            airplane = flight_plan['aircraft_short']
            departure = flight_plan['departure']
            arrival = flight_plan['arrival']
            print(f"{pilot['callsign']} ({pilot['cid']}) - {pilot['name']}")
            print(f"Departure - Arrival: {departure} - {arrival}")
            if flight_rule == 'I':
                print('Flight Rule: IFR')
            elif flight_rule == 'V':
                print('Flight Rule: VFR')
            print(f'Airplane: {airplane}')
            print(f'Route: {route}')
            ask_for_exit()

print('Created with love by Filippo Genoni')
ask_for_options()
