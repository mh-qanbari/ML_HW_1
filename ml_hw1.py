import csv


# [0] : Classes
class instance:
    # [FIELDS]
    i = int()
    b = bool()
# [/FIELDS]


# [0];

# [1] : Main Stream

with open('pregnancy_data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i = int(0)
    data = [1140, 10]
    for row in spamreader:
        print 'step_', i

        # row_cells = [10]
        row_cells = row[:]

        # [DEBUG]
        print 'row_cells:\t', row_cells
        print 'data:\t\t', data
        # [/DEBUG];

        # data[i] = list(row_cells)

        # for cell in row:
        # row_cells = cell.split(',')
        # print i, ', '.join(row)

        i = i + 1
        print

# [1];
