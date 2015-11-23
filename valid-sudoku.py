class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
    	rowset = set()
    	columnset = set()
    	for i in range(9):
    		rowset.clear()
    		columnset.clear()
    		for j in range(9):
    			if board[i][j] != '.':
	    			if board[i][j] in rowset:
	    				return False
	    			rowset.add(board[i][j])
    			if board[j][i] != '.':
    				if board[j][i] in columnset:
    					return False
    				columnset.add(board[j][i])
    	corner = set()
    	for cori in (0,3,6):
    		for corj in (0,3,6):
    			corner.clear()
    			for i in range(cori, cori+3):
    				for j in range(corj, corj+3):
    					if board[i][j] != '.':
    						if board[i][j] in corner:
    							return False
    						corner.add(board[i][j])
        return True

s = Solution()
b = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print s.isValidSudoku(b)