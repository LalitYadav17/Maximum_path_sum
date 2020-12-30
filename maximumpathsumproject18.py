number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
def list_converter(triangle_number):
    triangle_list=[]
    triangle_number=triangle_number.replace("\n"," ").split(" ")
    for i in range(1,16):
        list1=[]
        for j in range(i):
            list1.append(int(triangle_number[0]))
            del triangle_number[0]
        triangle_list.append(list1)
    return triangle_list


def maximum_total(triangle_list):
    for k in range(15,1,-1):
        list2=[]
        for l in range(k-1):
            if triangle_list[-1][l]+triangle_list[-2][l]>triangle_list[-1][l+1]+triangle_list[-2][l]:
                list2.append(triangle_list[-1][l]+triangle_list[-2][l])
            else:
                list2.append(triangle_list[-1][l+1]+triangle_list[-2][l])
        del triangle_list[-1]
        del triangle_list[-1]
        triangle_list.append(list2)
    print(triangle_list)




maximum_total((list_converter(number)))



