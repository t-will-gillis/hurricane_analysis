# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
updated_damages = []
for damage in damages:
    if damage == 'Damages not recorded':
        updated_damages.append('Damages not recorded')
    elif 'M' in damage:
        updated_damages.append(str(float(damage.strip('M'))*1000000))
    elif 'B' in damage:
        updated_damages.append(str(float(damage.strip('B'))*1000000000))
    else:
        updated_damages.append('Something went wrong')
print(updated_damages)


# write your construct hurricane dictionary function here:
hurricane_dictionary = {}
for i in range(len(names)):
    hurricane_dictionary[names[i]] = ({'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]})   
# print(hurricane_dictionary)


# write your count affected areas function here:
    # STRATEGY is to first create one list of only the areas
    # then create dictionary by going through list + counting occurences
areas_list = []
for areas in areas_affected:
    for area in areas:
        areas_list.append(area)

areas_occurences = {}
for i in range(len(areas_list)):
  if areas_list[i] in areas_occurences:
    continue
  else:
    areas_occurences[areas_list[i]] = areas_list.count(areas_list[i]) 
# print(areas_occurences) 


# write your find most affected area function here:
max_occurences = 0
most_affected_area = ''
for area, num in areas_occurences.items():
  if num > max_occurences:
    max_occurences = num
    most_affected_area = area
  else:
    continue
print('The area affected by the most hurricanes is {} with {} occurences noted.'.format(most_affected_area, max_occurences))


# write your greatest number of deaths function here:
max_deaths = 0
deadliest_hurricane = ''
for i in range(len(deaths)):
  if deaths[i] > max_deaths:
    max_deaths = deaths[i]
    deadliest_hurricane = names[i]
  else:
    continue
print('The deadliest hurricane in this record is {} with {} deaths noted.'.format(deadliest_hurricane, max_deaths))


# write your catgeorize by mortality function here:
mortality_ratings = {}
for i in range(6):
  mortality_ratings[i] = []
for i in range(len(hurricane_dictionary)):
  if hurricane_dictionary[names[i]]['Deaths'] == 0:
    mortality_ratings[0].append(hurricane_dictionary[names[i]])
  elif hurricane_dictionary[names[i]]['Deaths'] <= 100:
    mortality_ratings[1].append(hurricane_dictionary[names[i]])
  elif hurricane_dictionary[names[i]]['Deaths'] <= 500:
    mortality_ratings[2].append(hurricane_dictionary[names[i]])
  elif hurricane_dictionary[names[i]]['Deaths'] <= 1000:
    mortality_ratings[3].append(hurricane_dictionary[names[i]])
  elif hurricane_dictionary[names[i]]['Deaths'] <= 10000:
    mortality_ratings[4].append(hurricane_dictionary[names[i]])
  else:
    mortality_ratings[5].append(hurricane_dictionary[names[i]])


# write your greatest damage function here:
max_damage = 0
costliest_hurricane = ''
for i in range(len(hurricane_dictionary)):
  if (hurricane_dictionary[names[i]]['Damage']) == 'Damages not recorded':
    continue
  elif float(hurricane_dictionary[names[i]]['Damage']) > max_damage:
    max_damage = float(hurricane_dictionary[names[i]]['Damage'])
    costliest_hurricane = hurricane_dictionary[names[i]]['Name']
print('The costliest hurricane in this record is {} with damages of {} dollars noted.'.format(costliest_hurricane, max_damage))


# write your catgeorize by damage function here:
damage_scale = {}
for i in range(6):
  damage_scale[i] = []
for i in range(len(hurricane_dictionary)):
  if (hurricane_dictionary[names[i]]['Damage']) == 'Damages not recorded':
    continue
  elif float(hurricane_dictionary[names[i]]['Damage']) == 0:
    damage_scale[0].append(hurricane_dictionary[names[i]])
  elif float(hurricane_dictionary[names[i]]['Damage']) <= 10000000:
    damage_scale[1].append(hurricane_dictionary[names[i]])
  elif float(hurricane_dictionary[names[i]]['Damage']) <= 100000000:
    damage_scale[2].append(hurricane_dictionary[names[i]])
  elif float(hurricane_dictionary[names[i]]['Damage']) <= 1000000000:
    damage_scale[3].append(hurricane_dictionary[names[i]])
  elif float(hurricane_dictionary[names[i]]['Damage']) <= 5000000000:
    damage_scale[4].append(hurricane_dictionary[names[i]])
  else:
    damage_scale[5].append(hurricane_dictionary[names[i]])

# print(damage_scale[5])
