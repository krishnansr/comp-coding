ri_map = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000,
}
    
class Solution:
    def romanToInt(self, s: str) -> int:
        int_values = [ri_map[_char] for _char in s]
        
        val= 0
        i = 0
        while i < len(int_values):
            if i == len(int_values) - 1 or int_values[i] >= int_values[i+1]:
                val += int_values[i]
            else:
                val += int_values[i+1] - int_values[i]
                i += 1
            i += 1
                
        return val            
        
        