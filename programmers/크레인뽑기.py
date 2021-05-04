"""
크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 
아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. 
(그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 
크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 
터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

[제한사항]
board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
0은 빈 칸을 나타냅니다.
1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
moves 배열의 크기는 1 이상 1,000 이하입니다.
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
입출력 예
board	moves	result
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4
입출력 예에 대한 설명
입출력 예 #1

인형의 처음 상태는 문제에 주어진 예시와 같습니다. 크레인이 [1, 5, 3, 5, 1, 2, 1, 4] 번 위치에서 
차례대로 인형을 집어서 바구니에 옮겨 담은 후, 상태는 아래 그림과 같으며 바구니에 담는 과정에서 
터트려져 사라진 인형은 4개 입니다.

"""

def solution(board, moves):
    #answer = 0
    #return answer
    print(board,moves)
    
    print(board[2][1]) ##board[2][moves]
    ans = []
    
    #뽑기
    for m in moves:
        print('m > ',m)    
        for i in range(len(board)):
            #print('i > ',i)
            if board[i][m-1] != 0:
                print('out> ',board[i][m-1])
                temp = board[i][m-1]
                board[i][m-1] = 0
                ans.append(temp)   
                break
    print(ans)

    #같은거 지우기
    #한번만 반복함
    same = []
    for i in range(len(ans)-1):
        print('i > ', ans[i],ans[i+1])
        if ans[i] == ans[i+1]:
            #ans.remove(ans[i])
            #print(ans[i],ans[i+1])
            same.append(ans[i])
            same.append(ans[i+1])
            ans.remove(ans[i+1])
            ans.remove(ans[i])
            #i=0
            break
        i=0
    print(ans)
    print(same,len(same))
    
    
print(solution([[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]],[1,5,3,5,1,2,1,4]))