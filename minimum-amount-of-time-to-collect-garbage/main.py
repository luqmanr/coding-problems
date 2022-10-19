class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_last_stop = 0
        g_time = 0
        p_last_stop = 0
        p_time = 0
        m_last_stop = 0
        m_time = 0
        for i,gbg in enumerate(garbage):
            for char in gbg:
                if char == "G":
                    g_time += 1
                    g_last_stop = i
                elif char == "P":
                    p_time += 1
                    p_last_stop = i
                else:
                    m_time += 1
                    m_last_stop = i
        
        for stop in range(g_last_stop):
            g_time += travel[stop]
        
        for stop in range(p_last_stop):
            p_time += travel[stop]

        for stop in range(m_last_stop):
            m_time += travel[stop]
            
        return g_time + p_time + m_time