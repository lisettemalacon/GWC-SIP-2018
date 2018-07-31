names_ages = {
    'Lisette':16,
    'Karen':21,
    'Edward':19,
    'Mercedes': 46,
    'Eduardo':51
    }

print(names_ages)

total_age = 0

for key,value in names_ages.items():
    total_age += value

print(total_age/len(names_ages))
