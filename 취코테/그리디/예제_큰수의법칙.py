n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

#내림차순으로 정렬
data.sort(reverse=True)

count = m // (k+1) * k + m % (k+1)

result += count * data[0]
result += (m - count) * data[1]

print(result)

#오름차순으로 정렬
# data.sort()
#
# first = data[n-1]
# second = data[n-2]
#
# count = int(m/(k+1))*k
# count += m%(k+1)
#
# result = 0
# result += (count) * first
# result += (m-count) * second
#
# print(result)