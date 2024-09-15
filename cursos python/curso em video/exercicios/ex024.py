C = str(input('Em que cidade você nasceu? ')).strip()
print(C[:5].lower() == 'santo')
T = C.lower().find('santo')
print(T)