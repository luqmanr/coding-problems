class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) == 0:
            if n == 1:
                return n
            return -1
        people = []
        for trust_list in trust:
            people.append(trust_list[0])
            people.append(trust_list[1])
        people = set(people)
        
        for person in people:
            trust_counter = 0
            for trust_list in trust:
                if person == trust_list[1]:
                    trust_counter += 1
            if trust_counter == len(people)-1:
                for trust_list in trust:
                    if person == trust_list[0]:
                        return -1
                return person
            
        return -1