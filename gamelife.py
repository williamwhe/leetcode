import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        M=len(board)
        N=len(board[0])
        tmp=copy.deepcopy(board)
        for i in xrange(M):
            for j in xrange(N):
                neighbor=0
                if i>0:
                    neighbor+=board[i-1][j]
                if j<N-1:
                    neighbor+=board[i][j+1]
                if i<M-1:
                    neighbor+=board[i+1][j]
                if j>0:
                    neighbor+=board[i][j-1]
                if i>0 and j>0:
                    neighbor+=board[i-1][j-1]
                if i>0 and j<N-1:
                    neighbor+=board[i-1][j+1]
                if i<M-1 and j<N-1:
                    neighbor+=board[i+1][j+1]
                if i<M-1 and j>0:
                    neighbor+=board[i+1][j-1]
                if board[i][j]==0 and neighbor==3:
                    tmp[i][j]=1
                elif board[i][j]==1 and (neighbor==2 or neighbor==3):
                    tmp[i][j]=1
                else:
                    tmp[i][j]=0
        for i in xrange(M):
            for j in xrange(N):
                board[i][j]=tmp[i][j]
        print board
        
s=Solution()
s.gameOfLife([[1]])