class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_string = ""
        
        for char in s:
            if char.isalnum():
                cleaned_string += char

        
        prefix_pointer = 0
        postfix_pointer = len(cleaned_string)-1


        while prefix_pointer < postfix_pointer:
            if cleaned_string[prefix_pointer] != cleaned_string[postfix_pointer]:
                return False
            prefix_pointer +=1 
            postfix_pointer -=1
        return True

        