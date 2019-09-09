def Bubble_sort(items):
    for i in range(len(items)-1):
        flag=False                               #引入flag 若一次排序中没有一次变化，则判断排序结束利用break退出
        for j in range(0,len(items)-1-i):
            if items[j]>items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]
                flag=True
        if flag==False:
            break
                                                                        #精妙之处，在一个循环中，分别进行一次从头到尾，从尾到头的排序，存在很大共性合二为一
        for j in range(len(items)-1,i,-1):  #倒序法！！！！！！
            if items[j] < items[j -1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                flag = True
        if flag == False:
            break
    return items
list=[6,2,3,5,9,7,12]
print(Bubble_sort(list))
