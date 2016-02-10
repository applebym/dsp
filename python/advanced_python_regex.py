import re
import csv
import string

# class Professor(object):
#     """
#     Represents a Professor.
#
#     attributes: name, degree, title, email.
#     """
#
#     def __init__(self, name='', degree='', title='', email=''):
#         self.name = name
#         self.degree = degree
#         self.title = title
#         self.email = email
#
#     def __str__(self):
#         return str('Name: %s, Degree: %s, Title: %s, Email: %s' % \
#               (self.name, self.degree, self.title, self.email))
#
#     def get(self, attr):
#         if attr == 'name':
#             return self.name
#         if attr == 'degree':
#             return self.degree
#         if attr == 'title':
#             return self.title
#         if attr == 'email':
#             return self.email

def read_data(filename):
    with open(filename) as fp:
        reader = csv.reader(fp)
        data = list(reader)
        return data

# def create_profs(data):
#     prof_list = []
#     for i in range(1,len(data)):
#         prof = Professor(data[i][0].strip(), data[i][1].strip(),
#                          data[i][2].strip(), data[i][3].strip())
#         prof_list.append(prof)
#     return prof_list

def clean_degrees(degs):
    new_degs = []
    for deg in degs.strip(string.whitespace).split(' '):
        deg_clean = deg.replace('.', '').upper()
        new_degs.append(deg_clean)
    return new_degs


def make_degree_hist(data):
    dict = {}
    for prof in data[1:]:
        deg_list = clean_degrees(prof[1])
        for entry in deg_list:
            dict[entry] = dict.get(entry, 0) + 1
    del dict['0']
    return dict


def print_deg_freq(dict):
    for entry in dict:
        print entry + ' ' + str(dict[entry])


def main():
    data = read_data('faculty.csv')

    degrees_dict = make_degree_hist(data)
    print 'There are %d different degrees.' % (len(degrees_dict.keys()))
    print_deg_freq(degrees_dict)

if __name__ == '__main__':
    main()
