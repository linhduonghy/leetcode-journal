from typing import List  

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        times = [[time[0], time[1], index] for index, time in enumerate(times)]
        
        times.sort(key= lambda x: (x[0], x[1]))
        
        leave = [0]
        print(times)
        for i in range(len(times)):
            time = times[i]
            rem = -1
            max_pos_occupied = len(leave) 
            for j in range(0, max_pos_occupied):
                if time[0] >= leave[j]:
                    leave[j] = time[1]
                    rem = j
                    break
            if rem == -1:
                leave.append(time[1])
                rem = max_pos_occupied
            
            if time[2] == targetFriend:
                return rem
        
        return -1
        
            