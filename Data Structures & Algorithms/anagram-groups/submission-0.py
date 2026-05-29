class Solution:
    #The thought process I am having is to solve this in this order
    #First, create a dictionary. This will contain a string key and a value of string list.
    #When itrerating through the array, we will make the key the sorted version of the current word (if it does not exist yet), and the value be the word itself. 
    #If we come across a true anagram and the word has already been recorded, we append that to the value list.
    #If it is not there, we simply make another version. 
    #We combine all the list of strings together in a nested list and return that.
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        anagram_dict = {}

        for string in strs:
            sorted_str = str(sorted(string))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = [string]
            elif sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(string)
        
        for vals in anagram_dict.values():
            anagram_list.append(vals)
        return anagram_list