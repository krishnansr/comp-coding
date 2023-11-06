class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # O(N log N) solution
        # solution from https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/718239/Thinking-Process:-Greedy-Segment-Tree
        # using priority queues
        
        min_heap = []  # min heap of events end time
        events.sort(key = lambda e: e[0])  # sort events by start time

        i = count_events_attended = cur_day = 0
        while i < len(events) or min_heap:
            if not min_heap:
                cur_day = events[i][0]
            
            # add open events for cur_day
            while i < len(events) and events[i][0] <= cur_day:
                heappush(min_heap, events[i][1])
                i += 1

            heappop(min_heap)  # attend the event ends earliest
            count_events_attended += 1

            cur_day += 1
            # remove close events for cur_day
            while min_heap and min_heap[0] < cur_day:
                heappop(min_heap)

        return count_events_attended
    
    def maxEvents_old(self, events: List[List[int]]) -> int:
        # TLE exception for large arrays
        events.sort()  # sorted array is min_heap by start day
        
        attended = 1
        prev_day = heapq.heappop(events)[0]  # previous start day
        while events:
            print(len(events), attended)
            event_st, event_end = heapq.heappop(events)  # earliest possible event
            if event_st > prev_day:  # can attend
                attended += 1
                prev_day = event_st
            else:  # see if you can attend it in the future
                event_st_new = event_st + 1
                if event_st_new <= event_end:
                    heapq.heappush(events, [event_st_new, event_end])
        return attended