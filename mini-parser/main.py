# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

def nest_list(val, nested_int) -> list:
    obj = NestedInteger()
    obj.add(NestedInteger(val))
    obj.add(nested_int)
    return obj

class Solution:
    def deserialize(self, s: str) -> NestedInteger: 
        try:
            single_digit = int(s)
            return NestedInteger(single_digit)
        except:
            pass
        z = s.split("]")
        z = [val for val in z if val != '']
        print(z)
        z = z[0]
        z = z.split("[")
        z = [val for val in z if val != '']
        print(z)
        j = []
        for val in z:
            tmp = val.split(',')
            j.append(tmp[0])
        print(j)
        
        nested_list = NestedInteger()
        for i, num in enumerate(j[::-1]):
            if i == 0:
                nested_list = NestedInteger()
                nested_list.add(NestedInteger(int(num)))
                continue
            nested_list = nest_list(int(num), nested_list)
        
        return nested_list
        

# TODO: solve this puzzle, last tried 14/10/2022 - 16.03            
# input example: "[123,456,[788,799,833],[[]],10,[]]"
