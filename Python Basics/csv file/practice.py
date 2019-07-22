import csv

file1 = open('test.csv', 'r')

# reader generates an iterator. We can iterate through it to access the contents.
#csv_reader = csv.reader(file1, delimiter=',')

#We can use next to skip the beginning values.  next(iterator).
# for line in csv_reader:
# 	print(line)

#use of writer and writerow.
#file2 = open('written.csv', 'w')
#csv_writer = csv.writer(file2, delimiter='-')  #csv_writer is an object of class iterator.
#for line in csv_reader:
#	csv_writer.writerow(line)   #writerow is used to write row wise to the file. writerow is the method of the class writer.
#file2.close()                 #Always close the file after writing to it.

# csv_reader = csv.DictReader(file1, delimiter=',')    #csv_reader is the object of class iterator.
# for line in csv_reader:
#	del line['emali']       If we dont want to write any of the field onto the file.
# 	print(line)   now each line is an ordered dictionary instead of a list.
