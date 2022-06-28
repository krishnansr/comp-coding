class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_sum, res = sys.maxsize, []
        res_map = {hotel: i for i, hotel in enumerate(list1)}
            
        for j, hotel in enumerate(list2):
            i = res_map.get(hotel, None)
            if i is not None:
                if i + j > least_sum:
                    continue
                elif i + j < least_sum:
                    least_sum = i + j
                    res.clear()
                res.append(hotel)
        return res