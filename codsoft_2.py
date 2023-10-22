def add():
    a=int(input('Enter First Number: '))
    b=int(input('Enter Second Number: '))
    print(f'Result:{a+b}')
def sub():
    a=int(input('Enter First Number: '))
    b=int(input('Enter Second Number: '))
    print(f'Result:{a-b}')
def mul():
    a=int(input('Enter First Number: '))
    b=int(input('Enter Second Number: '))
    print(f'Result:{a*b}')
def div():
    a=int(input('Enter Nominator: '))
    b=int(input('Enter Denominator: '))
    if b == 0:
        print('Enter Non-Zero Number:(')
    else:
        print(f'Result:{a/b}')
print('*'*60,'SIMPLE CALCULATOR','*'*65)
while True:
    print('SELECT YOUR OPERATOR AS 1,2,3,4\n1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE')
    choice=input('ENTER YOUR CHOICE: ')
    if choice == '1':
        add()
    elif choice == '2':
        sub()
    elif choice == '3':
        mul()
    elif choice == '4':
        div()
    else:
        print('ENTER CORRECT OPERATOR:(')