import random
from abc import *
class MakeArray():
    def __init__(self):
        pass
    def Random_Arr(self,min_value=0,max_value=100,array_length=100):
        return [random.randint(min_value,max_value) for i in range(0,array_length)]




class Printfunc(object):
    def __init__(self,arr):
        self.arr = arr 

    def Before(self):
        print('Before Sorted')
        print(self.arr)
    
    def After(self):
        print('After Sorting')
        print(self.arr)
