"""
Reads the football.csv file and prints the name of the team with the
smallest difference in 'for' and 'against' goals (i.e. Goals minus Goals Allowed).
"""

import csv

def read_data(filename):
    with open(filename, 'rb') as fp:
        reader = csv.reader(fp)
        return list(reader)

def compute_score_diff(data):
    diff_list = []
    for i in range(1, len(data)):
        score_diff = abs(int(data[i][5]) - int(data[i][6]))
        diff_list.append((data[i][0],score_diff))
    return diff_list

def find_min_diff(scores):
    scores_sorted = sorted(scores, key=lambda x: x[1])
    return scores_sorted[0][0]

def main():
    data = read_data('football.csv')
    score_list = compute_score_diff(data)
    team = find_min_diff(score_list)
    print 'The team with the smallest difference is %s.' % team

if __name__ == '__main__':
    main()