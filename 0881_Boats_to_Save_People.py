class Solution(object):
    def numRescueBoats(self, people, limit):
        boat=0
        n=len(people)
        people.sort()
        left=0
        right=n-1
        while left<=right:
            if people[right]<=limit:
                if people[right]+people[left]<=limit:
                    left+=1
                boat+=1
                right-=1
            else:
                right-=1
                continue
        return boat
        
                    

        
