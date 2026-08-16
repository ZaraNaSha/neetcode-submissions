class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0
        while i<j and i < len(s):
            while not s[i].isalnum() and i<len(s)-1:
                i += 1
            while not s[j].isalnum() and j >0:
                j -= 1
            #print(s[i])
            #print(s[j])
            if (s[i].lower()!=s[j].lower()) and s[j].isalnum() and s[i].isalnum():
                return False
            i +=1
            j -=1
        return True
        