#open file excel
excelRead = open('./excel/excel.csv', mode='r', encoding='utf-8-sig')
#create file excel new
excelWrite = open('./excel/excel_new.csv', mode='w', encoding='utf-8-sig')

#read heading
line1 = excelRead.readline()

#write heading
excelWrite.writelines(line1.strip() + '; Điểm Trung Bình; Xếp Loại\n')

#read line2
line2 = excelRead.readline()

#loop line2
while line2 != "":

    #convert string to array
    list = line2.split(';')

    #define math
    math = float(list[2])
    #define lit
    lit = float(list[3])

    #grade point average
    ave = (math + lit) / 2
    #rounding
    ave = round(ave, 1)

    #define empty string
    rank = ''

    #condition
    if ave >= 8.0:
        rank = 'Giỏi'
    elif ave >= 6.5:
        rank = 'Tiên tiến'
    else:
        rank = 'Trung Bình'

    #write line2
    excelWrite.writelines(line2.strip() + ';' + str(ave) + ';' + rank + '\n')

    #read line2
    line2 = excelRead.readline()







