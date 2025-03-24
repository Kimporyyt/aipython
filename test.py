#num = int(input("출력할 구구단의 단을 입력하세요: ")) 
#number = input("구구단을 출력할 숫자를 입력하세요: ")

#print(f"{number}단:")
#print(number, "단:")
#print(number + "단:")
#print(number + "단, " + number + "단" + number + "단,")
#print(f"{number}단, {number}단  {number}단")
# number 값이 문자열이기 때문에 숫자로 변경해서 연산할 필요가 있다. int 없이 number=input(~~~)일 경우 해당 number 값이 2개씩 나오게 됨 
#따라서, int를 입력할 필요가 있다! 
s_number = input("구구단을 출력할 숫자를 입력하세요: ")
number = int(s_number)
result = number * 2
print(result)