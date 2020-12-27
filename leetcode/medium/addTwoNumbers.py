# Definition for singly-linked list.
import copy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_num_list(cls, ls_nums):
        obj = None
        for dig in ls_nums[::-1]:
            obj = cls(val=dig, next=obj)
        return obj

    def __repr__(self):
        print_str = list()
        temp_obj = self
        while True:
            print_str.append(temp_obj.val)
            if temp_obj.next is None:
                break
            temp_obj = temp_obj.next

        return str(print_str)


class Solution:
    def call_func(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_obj = ListNode()

        temp_obj = sum_obj
        digit_sum = 0
        while l1 or l2 or digit_sum:
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next
            temp_obj.next = ListNode(val=digit_sum % 10)
            temp_obj = temp_obj.next
            digit_sum //= 10

        return sum_obj.next

if __name__ == "__main__":
    l1_nums = [2,4,3] # for int 342
    l2_nums = [5,6,4] # for int 465
    # l1_nums = [9]
    # l2_nums = [1]
    # l1_nums = [9,9,9,9,9,9,9]
    # l2_nums = [9,9,9,9]

    l1 = ListNode.from_num_list(l1_nums)
    l2 = ListNode.from_num_list(l2_nums)
    args = [l1, l2]
    res = Solution().call_func(*args)
    print(res)

