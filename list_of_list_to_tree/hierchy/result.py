from typing import NoReturn


flat_hierarchy = [
    ['Europe', 'DE', 'Berlin', 'Wolfgang Muller'],
    ['Europe', 'DE', 'Berlin', 'Paul Geotze'],
    ['Europe', 'DE', 'Berlin', 'Julia Klopp'],
    ['Europe', 'DE', 'Karlsruhe', 'Jurgen Klopp'],
    ['Europe', 'DE', 'Karlsruhe', 'Felix Engel'],
    ['Europe', 'DE', 'Karlsruhe', 'Sebastian Walther'],
    ['Europe', 'UK', 'Borris Johnson'],
    ['Europe', 'UK', 'Harry Kane'],
    ['Africa', 'Sadio Mane'],
    ['Africa', 'Mo Salah'],
    ['North America', 'US', 'California', 'San Fransisco', 'Matt Smith'],
    ['North America', 'US', 'California', 'San Fransisco', 'Travis Noe'],
    ['North America', 'US', 'California', 'San Fransisco', 'Itan Chavira'],
    ['North America', 'US', 'California', 'San Fransisco', 'Travis Hawkins']
]

[['Europe', 'DE', 'Berlin', 'Wolfgang Muller'],
['Europe', 'DE', 'Berlin', 'Paul Geotze'], 
['Europe', 'DE', 'Berlin', 'Julia Klopp'], 
['Karlsruhe', 'Jurgen Klopp'], 
['Karlsruhe', 'Felix Engel'], 
['Karlsruhe', 'Sebastian Walther'], 
['UK', 'Borris Johnson'], ['UK', 'Harry Kane'], 
['Africa', 'Sadio Mane'], 
['Africa', 'Mo Salah'], 
['North America', 'US', 'California', 'San Fransisco', 'Matt Smith'], 
['North America', 'US', 'California', 'San Fransisco', 'Travis Noe'], 
['North America', 'US', 'California', 'San Fransisco', 'Itan Chavira'], 
['North America', 'US', 'California', 'San Fransisco', 'Travis Hawkins']]


data = {
    'Europe': {
        'DE': {
            'Berlin': ['Wolfgang Muller', 'Paul Geotze', 'Julia Klopp'],
            'Karlsruhe': ['Jurgen Klopp', 'Felix Engel', 'Sebastian Walther'],
        },
        'UK': ['Borris Johnson', 'Harry Kane'],
    },
    'Africa': ['Sadio Mane', 'Mo Salah'],
    'North America': {
        'US': {
            'California': {
                'San Fransisco': ['Matt Smith', 'Travis Noe', 'Itan Chavira', 'Travis Hawkins'],
            }
        }
    }
}

# print(keys)

top_list = []

def iter_data(items, new_list=[]):
    for item in items:
        new_list.append(item[0])
        if type(item[1]) == list:
            values = item[1]
            for value in values:
                nested_list = [*new_list]
                nested_list.append(value)
                top_list.append(nested_list)
        else:
            iter_data(item[1].items(), new_list)

        new_list = []
    return new_list


items = data.items()
iter_data(items)
print(top_list)

