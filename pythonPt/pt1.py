variable = 0; #자료형 업싱 변수선언가능 다른 자료형 할당가능
variable = variable + 5;
print(variable); 

a,b = input('숫자를 입력하세요').split(); #입력값 할당 공백을 기준으로 할당받음.

print(int(a), b) #형변환 이후 출력

c = list(range(5,11 ,2))
print(c)

lupa = {'name': 'shin', '키': 165, '몸무게': 65} #딕셔너리 만들기 c언어로 따지면 구조체???
print(lupa)