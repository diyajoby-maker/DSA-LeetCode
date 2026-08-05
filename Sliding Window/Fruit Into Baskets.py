class Solution(object):
    def totalFruit(self, fruits):
        win_count={}
        left=0
        ans=0
        for right in range(len(fruits)):
            win_count[fruits[right]]=win_count.get(fruits[right],0)+1
            while len(win_count)>2:
                win_count[fruits[left]]-=1
                if win_count[fruits[left]]==0:
                    del win_count[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
                           
                
