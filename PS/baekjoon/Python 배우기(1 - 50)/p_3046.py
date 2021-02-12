r1, s = map(int,(input().split()))

while(r1 <-1000 or r1 > 1000 or s <-1000 or s >1000):
    print("R1과 S는 -1000보다 크거나 같고, 1000보다 작거나 같습니다")
    r1, s = map(int,(input().split()))

print(2*s - r1)