class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode with length prefix and a delimiter to handle any character
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded_strs.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return decoded_strs