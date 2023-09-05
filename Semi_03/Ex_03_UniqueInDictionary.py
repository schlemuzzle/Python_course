# апишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

all_value = []
for now_dict in dictionary:
    for value in now_dict.values():
        all_value.append(value)
print(set(all_value))