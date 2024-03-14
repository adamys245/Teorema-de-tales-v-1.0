# script para me ajudar na tarefa da escola
def calculo():
    print('''                      a       c
                    ----    -----
                      b      d    ''')
    pergunta=str(input('Aonde é o x?: ').upper())
    # se X está na posicao a
    print('='*50)
    if pergunta=='A':
        a='x'
        b=int(input('Digite o valor B: '))
        c=int(input('Digite o valor C:'))
        d=int(input('Digite o valor D: '))
        print()
        # mostrar o calculo
        print(f'''                 {a}        {c}
                    ----    -----
                    {b}        {d}''')
        

        # calculo
        multiplicacao1=a*d
        multiplicacao2=b*c
        print(f'{d}{a} = {multiplicacao2}')
        print(f'{a} = {multiplicacao2} / {d}')
        print(f'{a} = {multiplicacao2/d}')
    if pergunta=='B':
        a=int(input('Digite o valor A: '))
        b='x'
        c=int(input('Digite o valor C:'))
        d=int(input('Digite o valor D: '))
        print()
        # mostrar o calculo
        print(f'''                 {a}        {c}
                    ----    -----
                    {b}        {d}''')
        

        # calculo
        multiplicacao1=c*b
        multiplicacao2=a*d
        print(f'{c}{b}= {multiplicacao2}')
        print(f'{b} = {multiplicacao2} / {c}')
        print(f'{b} = {multiplicacao2/c}')
    if pergunta=='C':
        a=int(input('Digite o valor A: '))
        b=int(input('Digite o valor B: '))
        c='x'
        d=int(input('Digite o valor D: '))
        print()
        # mostrar o calculo
        print(f'''                 {a}        {c}
                    ----    -----
                    {b}        {d}''')
        

        # calculo
        multiplicacao1=0
        multiplicacao2=a*d
        print(f'{b}{c}= {multiplicacao2}')
        print(f'{c} = {multiplicacao2} / {b}')
        print(f'{c} = {multiplicacao2/b}')
    if pergunta=='D':
        a=int(input('Digite o valor A: '))
        b=int(input('Digite o valor B: '))
        c=int(input('Digite o valor C:'))
        d='X'
        print()
        # mostrar o calculo
        print(f'''                 {a}        {c}
                    ----    -----
                    {b}        {d}''')
        

        # calculo
        multiplicacao1=d*a
        multiplicacao2=b*c
        print(f'{a}{d}= {multiplicacao2}')
        print(f'{d} = {multiplicacao2} / {a}')
        print(f'{d} = {multiplicacao2/a}')

calculo()