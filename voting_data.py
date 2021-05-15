voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.insert(1,{"county": "El Paso", "registered_voters":461149})

voting_data.pop(0)

voting_data.pop()

voting_data.insert(1,{'county': 'Jefferson', 'registered_voters': 432438})

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

#print(voting_data)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):

#       print(voting_data)


# for i in range(len(voting_data)):

#       print(voting_data[i])



#print Key and Values seperately
# for a in voting_data:
#     for b in a.values():
#         print(b)

#Printing Key, value and dict 

# for county_dict in voting_data:
#     print(county_dict['county'])


# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# for county_dict in voting_data:
#     print(county_dict)

