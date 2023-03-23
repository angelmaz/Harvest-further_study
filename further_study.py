from harvest import (make_melon_type_lookup, make_melon_types, Melon, get_sellability_report)

melon_types = make_melon_types()
melons_by_code = make_melon_type_lookup(melon_types)

harvest_melons = []

file = open('harvest_log.txt')
for line in file:
    words = line.split(" ")
    code = words[5]
    if code not in melons_by_code:
        print(f"Type {code} doesn't exist.")
        continue
    melon_type = melons_by_code[code]
    shape_rating = int(words[1])
    color_rating = int(words[3])
    harvested_field = words[11]
    harvested_person = words[8]
    harvest_melons.append(Melon(melon_type, shape_rating, color_rating,harvested_field, harvested_person))


get_sellability_report(harvest_melons)
