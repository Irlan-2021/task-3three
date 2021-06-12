import os
way = os.getcwd()
list_files = []
list_values = []
for filename in os.listdir(way):
    number_line = 0
    if filename.endswith(".txt"):
        list_files.append(filename)
        with open(filename, encoding='utf-8') as f:
            for line in f:
                number_line +=1
            list_values.append(number_line)

dict_files = dict(zip(list_files,list_values))
sorted_dist_files = (sorted(dict_files, key=dict_files.get, reverse=False))


my_file = open('final_doc.txt', 'w', encoding='utf-8')
for file in sorted_dist_files:
    my_file.write(file)
    my_file.write('\n')
    my_file.write(str(dict_files[file]))
    my_file.write('\n')
    with open(file, encoding='utf-8') as f:
        data = f.read()
        my_file.write(data)
        my_file.write('\n')
my_file.close()
