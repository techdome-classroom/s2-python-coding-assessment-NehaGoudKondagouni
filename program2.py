class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
        total = 0
        length = len(s)
        
        for i in range(length):
            current_value = roman_dict[s[i]]
            
            if i + 1 < length and current_value < roman_dict[s[i + 1]]:
                total -= current_value
            else:
                total += current_value
        
        return total



