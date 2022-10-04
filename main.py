coun_part=int(input())
partspnt=[]
i=0

while i < coun_part:
    partspnt=input().split(',')
    fio=partspnt[0]+partspnt[1]+partspnt[2]
    lengfio = len(set(fio))
    if(int(partspnt[3])>=10 and int(partspnt[4])>=10):
        month=int(partspnt[3][0])+int(partspnt[3][1])+int(partspnt[4][0])+int(partspnt[4][1])
    if (int(partspnt[3]) >= 10 and int(partspnt[4]) < 10):
        month = int(partspnt[3][0])+int(partspnt[3][1])+int(partspnt[4])
    if (int(partspnt[3]) < 10 and int(partspnt[4]) >= 10):
        month = int(partspnt[3])+int(partspnt[4][0])+int(partspnt[4][1])
    if (int(partspnt[3]) < 10 and int(partspnt[4]) < 10):
        month = int(partspnt[3]) + int(partspnt[4])
    n_f_c=ord((partspnt[0][0]).lower())-96
    sum = lengfio+month*64+n_f_c*256
    code= (f'{sum:x}').upper()
    if(len(code)>=3):
        print(code[-3]+code[-2]+code[-1])
    if(len(code)==2):
        print('0'+code)
    if(len(code)==1):
        print('0'+'0'+code)

    i+=1
