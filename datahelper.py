import csv
import constants

def read_uid_list(filename):

    with open(filename, 'r') as db:
        reader = csv.DictReader(db)
        data = list(reader)
    return data

def check_uid_list(filename, uid):
    try:
        with open(filename, 'r') as db:
            reader = csv.DictReader(db)
            for row in reader:
                if row['uid'] == uid:
                    return True
    except FileNotFoundError: 
        print(f'ERROR: {filename} not found...')
    except KeyError:
        print('ERROR: UID column not found in the csv file')
    return False

def add_uid_to_list(filename, uid, check_value=True):
    data = read_uid_list(filename)
    data.append({'UID': uid, 'Check': check_value})
    write_csv(filename, data)

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)