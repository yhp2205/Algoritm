#하노이의 탑
#input: 옮기려는 원반의 갯수 n
#       옮길 원반이 현재 있는 출발점 기둥 from_pos
#       원반을 옮길 도착점 기둥 to_pos
#       옮기는 과정에서 사용할 보조기둥 aux_pos

def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:
        print(from_pos, "->", to_pos)
        return

    #원반 n-1개를 aux_pos로 이동
    hanoi(n-1, from_pos, aux_pos, to_pos)
    #가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos)
    #aux_pos에 있는 원반 n-1개를 목적지로 이동
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n=1")
hanoi(1, 1, 3, 2)
print("n=2")
hanoi(2, 1, 3, 2)
print("n=3")
hanoi(3, 1, 3, 2)
