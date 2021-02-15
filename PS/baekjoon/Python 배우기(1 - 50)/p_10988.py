word = input()

mid = len(word)//2
is_palindrome = 1  #한글자 단어도 펠린드롬으로 출력해야 하므로 초기값을 1로 설정
for i in range(mid):

    if word[i] == word[-i-1]:
        is_palindrome = 1

    elif word[i] != word[-i-1]:
        is_palindrome = 0
        break

print(is_palindrome)