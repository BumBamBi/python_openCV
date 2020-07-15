import numpy as np

a = np.array([1, 2, 3, 4])

# 쓰레기
b = np.empty((2, 3));

# b의 모든 요소 100으로 채우기
b = b.fill(100);

# 0으로 채우
c = np.zeros((2, 3));

# 1로 채우기
d = np.ones((2, 3));

# 원하는 값으로 채우기
e = np.full((2, 3, 4), 255, dtype=np.uint8);

#np.----_like(???) 를 하면, ????와 같은 size로 만듬

# 0부터 시퀀스하게 5개 원 생성 (괄호안을 float로 주면 float으로 나옴)
f = np.arange(5)

# 시작, 끝, 간격 으로 생성 -> 끝은 출력 x
g = np.arange(3,9,2)

# 2~3 사이의 무작위
h = np.random.rand(2, 3)

# 2~3 사이의 가우스분포
i = np.random.randn(2, 3)

# 데이터형식 바꾸기
j = i.astype(int)

# 배열 모양 바꾸기
k = j.reshape(2, 3)
k = np.reshape(k, (2, 3))

# -1을 하면,알아서 차수를 맞춰달라
l = np.arange(100).reshape(2, -1)

# 1xN의 1차원 행렬로 변경하기
m = np.ravel(l)

# 행렬 모양 뒤집기 => 매트랩의 '
n = m.T

# 브로드캐스팅 연산 -> SIMD 같은거임 벡테연산법
# 배열끼리의 연산도 가능하나, 제약이 있음 (동일 모양 or 한 배열이 1차원이고, N의 개수 동)
o = np.arange(10)
o = (o*4-1)/2
o = o > 3


# np에서 []로 뽑아낸 값은 복사본이 아니라 원본임...!
p = np.arange(6).reshape(2, 3)
pp = p[0:2, 1:3]
pp[0] = 99
print(p)

# list 처럼 복사본을 얻고싶다면, ndarray.copy()를 써야함

# 조건을 주고 조건에 맞는 값들만 가져오기 가능
q = np.arange(10)
qq = q > 5
print(qq)
print(q[qq])

q[qq] = 1
print(q)

q = np.arange(12).reshape(3, 4)
print(q[[0, 2]])

# 병합
r1 = np.arange(4).reshape(2, 2)
r2 = np.arange(4, 8).reshape(2, 2)
# 세로 병합
print(np.vstack((r1, r2)))
# 가로 병합
print(np.hstack((r1, r2)))
# 가로/세로 병합
print(np.concatenate((r1, r2), 0))
print(np.concatenate((r1, r2), 1))
# RGB 처럼 3차원 축 병합
r3 = np.stack((r1, r2), 0)
print(r3.shape)
# 1이면 가로 한 축씩 병합, 2면 세로 한축씩 병합

# 분리
s = np.arange(12)
# 3등분
print(np.split(s, 3))
# :,3 3,6 6,:
print(np.split(s, [3, 6]))

s = s.reshape(4, 3)
# 가로 두개로 쪼개기
print(np.vsplit(s, 2))
# 세로 1개만 따로 쪼개고 나머지
print(np.hsplit(s, [1]))

# 검색
t = np.arange(10, 20)
# 15 이상 인덱스 검출
print(np.where((t > 15)))
# 15 이상 인덱스 1, 0 으로 나눔
print(np.where((t > 15), 1, 0))
# 15 이상은 그대로 두고, 나머진 0으로
print(np.where((t > 15), t, 0))

# 조건만 이용해서 사용하면, x, y 좌표 인덱스가 검출
tt = np.arange(12).reshape(3, 4)
print(np.where(tt > 6))
# 이를 np.stack 을 이용하여 좌표 변환 가능
tt_xy = np.where(tt > 6)
print(np.stack((tt_xy[0], tt_xy[1]), 1))

# 0이 아닌 원소의 인덱스
u = np.arange(10)
u = np.where((u > 5), 1, 0)
print(np.nonzero(u))
# stack으로 합치기 가능
uu = ([0, 1, 2], [3, 0, 4], [5, 6, 0])
uu_xy = np.nonzero(uu)
print(np.stack((uu_xy[0], uu_xy[1]), 1))

# 모든 요소 T/F 일괄 확인
v1 = np.arange(10)
v2 = np.arange(10)
print(np.all(v1))
print(np.all(v1 == v2))
# 다른 위치 찾기
v2[0] = 1
print(np.where(v1 != v2))

# 합, 평균, 최대, 최소
w = np.arange(10)
print(np.sum(w))
print(np.mean(w))
print(np.max(w))
print(np.min(w))

