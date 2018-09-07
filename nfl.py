# focuse on enumerate()
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def column(self, label):
        if label not in self.header:
            return None
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')
print(year_column)
print(player_column)
'''out put 
will show every years like:['2009',......]'''

# lastest practice in this chapter
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def __str__(self):
        data_string = self.data[:10]
        return str(data_string)

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column

    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)

'''output
[['2009', '1', 'Pittsburgh Steelers', 'Tennessee Titans'], 
 ['2009', '1', 'Minnesota Vikings', 'Cleveland Browns'], 
 ['2009', '1', 'New York Giants', 'Washington Redskins'], 
 ['2009', '1', 'San Francisco 49ers', 'Arizona Cardinals'], 
 ['2009', '1', 'Seattle Seahawks', 'St. Louis Rams'], 
 ['2009', '1', 'Philadelphia Eagles', 'Carolina Panthers'], 
 ['2009', '1', 'New York Jets', 'Houston Texans'], 
 ['2009', '1', 'Atlanta Falcons', 'Miami Dolphins'], 
 ['2009', '1', 'Baltimore Ravens', 'Kansas City Chiefs'], 
 ['2009', '1', 'Indianapolis Colts', 'Jacksonville Jaguars']]'''