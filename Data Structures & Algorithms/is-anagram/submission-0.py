class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_list = list(s)
            t_list = list(t)
            for i in s_list:
                if i in t_list:
                    t_list.remove(i)
                else:
                    return False
            if len(t_list) == 0:
                return True
            else:
                return False
