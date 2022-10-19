class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_time = [0, 0]
        p_time = [0, 0]
        m_time = [0, 0]
        curr_time = 0
        for i,gbg in enumerate(garbage):
            if i > 0:
                curr_time += travel[i-1]
            if "G" in gbg:
                g_time[0] += gbg.count("G")
                g_time[1] = curr_time
            if "P" in gbg:
                p_time[0] += gbg.count("P")
                p_time[1] = curr_time
            if "M" in gbg:
                m_time[0] += gbg.count("M")
                m_time[1] = curr_time
                
        return (g_time[0] + g_time[1]) + (p_time[0] + p_time[1]) + (m_time[0] + m_time[1])