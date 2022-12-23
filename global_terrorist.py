with open('terrorist.txt', 'r') as file:
    sums = {}
    similarity_id = 1
    serial_number = 1
    
    for line in file:
        values = [int(x) for x in line.split(',')]
        line_sum = sum(values)
        
        if line_sum in sums:
            sums[line_sum]['count'] += 1
            sums[line_sum]['similarity_id'] = similarity_id
        else:
            sums[line_sum] = {'count': 1, 'similarity_id': similarity_id}
            similarity_id += 1
        serial_number += 1

serial_number = 1

print('Serial Number'.ljust(20), 'SUM'.ljust(20), 'Similarity Id'.ljust(20))
for sum_, data in sums.items():
    print(str(serial_number).ljust(20), str(sum_).ljust(20), str(data["similarity_id"]).ljust(20))
    serial_number += 1
