#Radix Sort
# 
import numpy as np 
from setting import MakeArray, Printfunc

MIN = 0
MAX = 100
ARRAY_SIZE = 100

arr = MakeArray().Random_Arr(MIN,MAX,ARRAY_SIZE)

class RadixSort(object):
    def __init__(self,arr):
        self.arr = arr 
    def Sorting(self):
        def digits(idx,pos):
            div_num = int(idx/pos)
            index = div_num %10 
            return div_num, index
        position = 1
        while True:
            bucket = [list() for _ in range(10)]
            is_sorted = True            
            for i in arr:
                div_num, index = digits(i,position)
                bucket[index].append(i)
                if div_num >= 10:
                    is_sorted = False 
            position *= 10
            arr.clear() 
            for numbers in bucket:
                for num in numbers:
                    arr.append(num)
                    
            if is_sorted:
                return arr


p = Printfunc(arr)
p.Before()
sort = RadixSort(arr).Sorting()
p.After()