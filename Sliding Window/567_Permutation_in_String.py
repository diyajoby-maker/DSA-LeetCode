class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        win_count={}
        p_count={}
        for ch in s1:
            p_count[ch]=p_count.get(ch,0)+1
        left=0
        for right in range(len(s2)):
            win_count[s2[right]]=win_count.get(s2[right],0)+1
            if right-left+1>len(s1):
                win_count[s2[left]]-=1
                if win_count[s2[left]]==0:
                    del win_count[s2[left]]
                left+=1
            if p_count==win_count:
                return True
        return False
