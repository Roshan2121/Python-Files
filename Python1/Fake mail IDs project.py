import random
list1 = ['Harsh', 'ewweuf', 'wuef', 'wedmv', 'bnmbv', 'snmvv', 'cnxzcad', 'dvbvdsjvsd', 'hvsfdshf', 'sdfha', 'wofhe', 'dfvnbv']
list2 = ['234', '452', '896', '610', '233', '788', '123', '111', '12', '21', '678', '900', '569', '432', '562', '432', '566', '211', '557', '965']
Name = random.choice(list1)
Number = random.choice(list2)
list3 = [Name, Number, '@gmail.com']
delimiter = ""
string = delimiter.join(list3)
print(string)


    
    
