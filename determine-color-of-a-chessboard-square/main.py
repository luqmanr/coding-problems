class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # flip/switch True & False
        def switch(mode):
            if mode is True:
                return False
            return True
        mode = False

        # create chess board definition
        row_size = 8
        code = "abcdefgh"
        for i in range(1, row_size+1):
            for k in code:
                # if input coordinates equals chessboard code
                if coordinates == k + str(i):
                    return mode
                mode = switch(mode)
            mode = switch(mode)
            
        # if input coordinates is not in chessboard
        return False