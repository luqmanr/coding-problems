class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        alice_arrive_month = int(arriveAlice[:2])
        alice_arrive_day   = int(arriveAlice[3:5])
        alice_arrive_count = 0
        for i in range(alice_arrive_month):
            if i == alice_arrive_month-1:
                alice_arrive_count += alice_arrive_day
            else:    
                alice_arrive_count += months[i]
           
        alice_leave_month = int(leaveAlice[:2])
        alice_leave_day   = int(leaveAlice[3:5])
        alice_leave_count = 0
        for i in range(alice_leave_month):
            if i == alice_leave_month-1:
                alice_leave_count += alice_leave_day
            else:
                alice_leave_count += months[i]
                
        bob_arrive_month = int(arriveBob[:2])
        bob_arrive_day   = int(arriveBob[3:5])
        bob_arrive_count = 0
        for i in range(bob_arrive_month):
            if i == bob_arrive_month-1:
                bob_arrive_count += bob_arrive_day
            else:    
                bob_arrive_count += months[i]
           
        bob_leave_month = int(leaveBob[:2])
        bob_leave_day   = int(leaveBob[3:5])
        bob_leave_count = 0
        for i in range(bob_leave_month):
            if i == bob_leave_month-1:
                bob_leave_count += bob_leave_day
            else:
                bob_leave_count += months[i]
        
        if alice_arrive_count <= bob_arrive_count <= alice_leave_count:
            time_diff = alice_leave_count - bob_arrive_count + 1
            if bob_leave_count < alice_leave_count:
                time_diff += (bob_leave_count - alice_leave_count)
            return time_diff
        elif bob_arrive_count <= alice_arrive_count <= bob_leave_count:
            time_diff = bob_leave_count - alice_arrive_count + 1
            if alice_leave_count < bob_leave_count:
                time_diff += (alice_leave_count - bob_leave_count)
            return time_diff
        else:
            return 0