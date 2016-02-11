import advanced_python_regex as apr
from collections import defaultdict

def get_first(prof):
    first = prof[0].split()[0]
    return first

def get_last(prof):
    last = prof[0].split()[-1]
    return last

def get_degree(prof):
    degree = prof[1].strip()
    return degree

def get_title(prof):
    title = prof[2].split()[:-2]
    return ' '.join(title)

def get_email(prof):
    email = prof[3]
    return email

def make_faculty_dict(data):
    dict = defaultdict(list)
    for prof in data[1:]:
        last = get_last(prof)
        degree = get_degree(prof)
        title = get_title(prof)
        email = get_email(prof)
        dict[last].append([degree, title, email])
    return dict


def make_prof_dict(data):
    dict = {}
    for prof in data[1:]:
        name = (get_first(prof), get_last(prof))
        degree = get_degree(prof)
        title = get_title(prof)
        email = get_email(prof)
        dict[name] = [degree, title, email]
    return dict


def print_dict(dict, num):
    for key in dict.keys()[:num]:
        print key
        print dict[key]
        print ' '

def print_dict_sort_last(dict, num):
    name_sort = sorted(dict.keys(), key=lambda name: name[1])
    for key in name_sort[:3]:
        print key
        print dict[key]
        print ' '

def main():
    data = apr.read_data('faculty.csv')

    # Q6
    faculty_dict = make_faculty_dict(data)
    print_dict(faculty_dict, 3)

    # Q7
    professor_dict = make_prof_dict(data)
    print_dict(professor_dict, 3)

    # Q8
    print_dict_sort_last(professor_dict, 3)

if __name__ == '__main__':
    main()