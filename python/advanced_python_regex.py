import csv
import string

def read_data(filename):
    with open(filename) as fp:
        reader = csv.reader(fp)
        data = list(reader)
        return data

def clean_degrees(degs):
    new_degs = []
    for deg in degs.strip(string.whitespace).split(' '):
        deg_clean = deg.replace('.', '').upper()
        new_degs.append(deg_clean)
    return new_degs

def make_hist(data, num):
    dict = {}
    for prof in data[1:]:
        if num == 1:
            dl = clean_degrees(prof[num])
            for entry in dl:
                dict[entry] = dict.get(entry, 0) + 1
        elif num == 2:
            dict[prof[num]] = dict.get(prof[num], 0) + 1
    if num == 1:
        del dict['0']
    if num == 2:
        del dict['Assistant Professor is Biostatistics']
        dict['Assistant Professor of Biostatistics'] = dict.get('Assistant Professor of Biostatistics', 0) + 1
    return dict

def print_freq(dict):
    for entry in dict:
        print entry + ' ' + str(dict[entry])

def get_emails(data):
    email_list =[]
    for prof in data[1:]:
        email_list.append(prof[3])
    return email_list

def print_list(list):
    for item in list:
        print item

def get_domains(email_list):
    domain_list = []
    dict = {}
    for item in email_list:
        name, domain = item.split('@')
        domain_list.append(domain)
    for item in domain_list:
        dict[item] = dict.get(item, 0) + 1
    return dict.keys()

def main():
    data = read_data('faculty.csv')

    degrees_dict = make_hist(data, 1)
    print 'There are %d different degrees.' % (len(degrees_dict.keys()))
    print_freq(degrees_dict)

    print ' '

    titles_dict = make_hist(data, 2)
    print 'There are %d different titles.' % (len(titles_dict.keys()))
    print_freq(titles_dict)

    print ' '

    email_list = get_emails(data)
    print_list(email_list)

    print ' '

    domain_list = get_domains(email_list)
    print 'There are %d different domains.' % (len(domain_list))
    print_list(domain_list)

if __name__ == '__main__':
    main()
