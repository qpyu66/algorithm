"""
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

"""


# code refactoring
def solution(answers):
    answer = []
    #per = {1:"1,2,3,4,5"}
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    count01 = 0
    count02 = 0
    count03 = 0
    ans = []
    
    
    
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            count01 += 1
        if answers[i] == two[i%len(two)]:
            count02 += 1
        if answers[i] == three[i%len(three)]:
            count03 += 1    
    ans = [count01,count02,count03]
    
    print('ans > ',ans)
    
    for idx,val in enumerate(ans):
        print('idx > ',idx,', val > ',val)
        if val == max(ans):
            answer.append(idx+1)
    
    
    print(answer)
    #return answer


print(solution([1,2,3,4,5])) #1
print(solution([1,3,2,4,2])) #1,2,3