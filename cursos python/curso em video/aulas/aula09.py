print('fatiamento')
frase = str(input('Digite uma frase:'))
frase2 = '  Curso em Video python  '
print(frase)
print(frase2)
print(frase[9])
print(frase[9:13])
print(frase[5:9:2])
print(frase[4:])
print(frase[:7])
print(frase[5::3])
print(len(frase)) #comprimento da frase
print(frase.count('a',0, 10)) #contador de letra
print(frase2.find('deo'))
print(frase2.find('android'))
print('curso' in frase2) #posição da palavra
print(frase2.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #deixa a primeira letra em maiúscula
print(frase.title()) #capitalize palavra por palavra
print(frase2.strip()) #remove espaços inúteis no inicio e fim da frase
print(frase2.rstrip()) #somente lado direito de right 
print(frase2.lstrip()) #somente lado esquerdo de left
print(frase.split()) #vai separar as frases em palavras individuais
print('-'.join(frase)) #inclui entre os espaços
print("""Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil, aliquid, perferendis recusandae, eveniet quasi non corporis perspiciatis maxime quo ad quisquam saepe possimus ipsum vitae illo quibusdam nam voluptatum voluptas!
</body>""") #""" escreve o texto como ele é