import csv

import numpy as np

DISTANCE = 7


# categories indexes
# rdul = 0
# rdlu = 1
# drul = 2
# drlu = 3
# ludr = 4
# lurd = 5
# uldr = 6
# ulrd = 7
#
# manh = 0
# hamm = 1


def split_data(table):
    rdul = []
    rdlu = []
    drul = []
    drlu = []
    ludr = []
    lurd = []
    uldr = []
    ulrd = []
    for row in table:
        strategy = row[3]
        temp = [row[0], row[4], row[5], row[6], row[7], row[8]]
        if strategy == "rdul":
            rdul.append(temp)
        elif strategy == "rdlu":
            rdlu.append(temp)
        elif strategy == "drul":
            drul.append(temp)
        elif strategy == "drlu":
            drlu.append(temp)
        elif strategy == "ludr":
            ludr.append(temp)
        elif strategy == "lurd":
            lurd.append(temp)
        elif strategy == "uldr":
            uldr.append(temp)
        elif strategy == "ulrd":
            ulrd.append(temp)

    return [rdul, rdlu, drul, drlu, ludr, lurd, uldr, ulrd]


def split_astr(table):
    manh = []
    hamm = []
    for row in table:
        temp = [row[0], row[4], row[5], row[6], row[7], row[8]]
        strategy = row[3]
        if strategy == "manh":
            manh.append(temp)
        elif strategy == "hamm":
            hamm.append(temp)

    return [manh, hamm]


def general_trim(table):
    data = [[] for _ in range(DISTANCE)]
    for row in table:
        data[row[0] - 1].append(np.array(row[1:]))
    return data


def calculate(table):
    data = []
    for i in range(len(table)):
        data.append(np.divide(np.sum(table[i], axis=0), len(table[i])))
    return np.array(data)


def categorised_avg(table):
    category = []
    category_avg = []
    for x in range(len(table)):
        category.append(general_trim(table[x]))
        category_avg.append(calculate(category[x]))
    return category_avg


def general_avg(table):
    general_sum = [np.array([table[i][x] for i in range(len(table))]) for x in range(DISTANCE)]
    distance_category_avg = []
    for i in range(len(general_sum)):
        distance_category_avg.append(np.divide(np.sum(general_sum[i], axis=0), len(general_sum[i])))
    return distance_category_avg


def get_data(table, index):
    return [table[i][index] for i in range(len(table))]


def read_file(file):
    data = []
    with open(file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        for row in csvreader:
            data_row = [int(row[0]), int(row[1]), row[2], row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7]),
                        float(row[-1])]
            data.append(data_row)

    return data


filename = 'Data.csv'

array = read_file(filename)
bfs = []
dfs = []
astr = []
for r in array:
    if r[2] == 'astr':
        astr.append(r)
    if r[2] == 'bfs':
        bfs.append(r)
    if r[2] == 'dfs':
        dfs.append(r)

bfs_categorised = split_data(bfs)
dfs_categorised = split_data(dfs)
astr_categorised = split_astr(astr)

bfs_strategy_avg = categorised_avg(bfs_categorised)
bfs_general_avg = general_avg(bfs_strategy_avg)

dfs_strategy_avg = categorised_avg(dfs_categorised)
dfs_general_avg = general_avg(dfs_strategy_avg)

astr_strategy_avg = categorised_avg(astr_categorised)
astr_general_avg = general_avg(astr_strategy_avg)

for line in bfs_general_avg:
    print(line)
print()

for line in dfs_general_avg:
    print(line)
print()

for line in astr_general_avg:
    print(line)
