#Comando para abrir um arquivo o 'r' serve para apenas ler.
arquivo = open('alunos.txt','r')

Com o for, cada linha do arquivo será jogado para a variavel dado.
for dado in arquivo:
    print(dado)
arquivo.close()

#O parametro 'w' serve para escrever algo no arquivo(apagando), e o 'a' apenas adiciona, não exclui.
arquivo2 = open('alunos.txt', 'a')
arquivo2.write('Testeando inserção\n')
arquivo2.close()

#with serve para coisas automáticas, abrir e fechar uma função por exemplo.
#abertura do arquivo para gravação com fechamento automático.
with open('alunos.txt','a') as arquivo:
    arquivo.write('testando fechamento automático.')