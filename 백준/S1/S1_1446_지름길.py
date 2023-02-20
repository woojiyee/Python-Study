# 알고리즘
'''
1. 입력 받을시, 범위 밖은 저장 x
2. 이득 거리(범위 실 거리 - 지름길 거리)가 음수인 입력값도 저장 x
3. 입력 받을 시 이득 거리도 계산해서 같이 저장
4. 이득 거리 기준으로 내림 차순 정렬
5. 이득 거리가 큰 순으로 체킹(반복문 돌기)
6. 큐 저장 시, 이득 거리는 제외한 원소만 저장
7. if 현재 큐에 있는 원소의 시작값 > 체킹할 원소의 종료값
    leftappend
   elif 현큐 원소 종료값 < 체킹 원소 시작값
    append
   else
    continue
+
start = 0
dis = 0
while q:
    qStart, qEnd, qDis = q.popleft
    dis = qStart - start + qDis
    start = qEnd
'''