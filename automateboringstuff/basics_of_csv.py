import csv

example_file = open('example.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_reader)
print(example_data)

output_file = open('example2.tsv', 'w', newline='')
output_writer = csv.writer(output_file, delimiter= '\t', lineterminator= '\n\n')
output_writer.writerow(['Apple', 3, 0.73])
output_writer.writerow(['Salmon', 18.25, 3.5])
output_writer.writerow(['Milk', 6.5, 1])
output_writer.writerow(['Eggs', 1, 4.75])
output_writer.writerow(['Potato', 1.25, 1.25])

output_file.close()

output_file = open('sample.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['Item', 'Price', 'Qty'])
output_writer.writerow(['Apple', 3, 0.73])
output_writer.writerow(['Salmon', 18.25, 3.5])
output_writer.writerow(['Milk', 6.5, 1])
output_writer.writerow(['Eggs', 1, 4.75])
output_writer.writerow(['Potato', 1.25, 1.25])

output_file.close()