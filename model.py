#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

b_seasons = []

def init_bball(csv_file_name=BB_FILE_NAME):
    global b_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global b_seasons
        b_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            b_seasons.append(r)
def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortc = 1
    elif sortby == 'wins':
        sort = 3
    elif sortby == 'pct':
        sortc = 5
    else:
        sortc = 0
    rev = (sortorder == 'desc')
    sorted_list = sorted(b_seasons, key=lambda row: row[sortc], reverse=rev)
    return sorted_list
