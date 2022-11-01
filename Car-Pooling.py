class Solution(object):
    def carPooling(self, trips, capacity):
        list=[]
        for i in range(len(trips)):
            list.append([trips[i][1],1,trips[i][0]])
            list.append([trips[i][2],0,trips[i][0]])
        curr =0
        list=sorted(list)
        for i in range(len(list)):
            if list[i][1]==1:
                curr +=list[i][2]
            else:
                if list[i][1]==0:
                    curr -=list[i][2]
            if curr > capacity:
                return False
        
        return True
