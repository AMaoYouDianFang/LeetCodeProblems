class Solution(object):
    def multiply(self, A, B):

        m , n, nb, = len(A), len(B), len(B[0])  #m*n n*nb
        res = [[0]*nb for i in range(m)]    #m*nb

        idxA = []
        for i in range(m):
            tmp =[]
            for j in range(n):
                if A[i][j] !=0:
                    tmp.append(j)
            idxA.append(tmp)
        

        for i in range(m):
            for j in idxA[i]:
                for k  in range(nb):
                    res[i][k] += A [i][j] *B[j][k]
        
        return res

if __name__ == "__main__":
    A = [[ 1, 0, 0],[-1, 0, 3]]
    B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]   
    s =Solution()
    print(s.multiply(A,B))