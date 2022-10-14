class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        cards_ = {}
        for _,num in enumerate(cards):
            cards_[str(num)] = []
        for i,num in enumerate(cards):
            cards_[str(num)].append(i)
        
        min_length = [cards_[key] for i,key in enumerate(cards_) if len(cards_[key]) > 1]
        if len(min_length) == 0:
            return -1
        
        idx_lengths = []
        for idxs in min_length:
            for i,idx in enumerate(idxs):
                if i == len(idxs)-1:
                    break
                idx_lengths.append(idxs[i+1] - idx + 1)
        
        return min(idx_lengths)