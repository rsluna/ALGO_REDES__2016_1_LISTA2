Questão 01


c1=0
c2=0
c3=0

for i in range(10):
    nota=int(input('Qual Sua sensação após o filme?(1-normal, 2-boa, 3 ótima: )'))
    if nota==1:
            c1=c1+1
    elif nota==2:
            c2=c2+1
    elif nota==3:
            c3=c3+1
    else:
            print('Opção não é válida')

print(c1, ' Pessoa(s) Achou(aram) o Filme Regular.')
print(c2, ' Pessoa(s) Achou(aram) o Filme Normal.')
print(c3, ' Pessoa(s) Achou(aram) o Filme ótimo.')


Questão 02

algoritmo cinema
Declare c1, c2, c2 : inteiro
c1<-0
c2<-0
c3<-0 

Inicio

para i= 1 Ate 10 faça
	faça caso nota<-1
		  c1<-c1+1 
		 caso nota<-2
		  c2<-c2+1 
		 caso nota<-3 
		  c3<-c3+1 
	outro caso 
		  escrever('Entrada inválida')
		  
	fim de caso
	
	escreva(c1, 'Pessoas Acharam o filme regular')
	escreva(c2, 'Pessoas Acharam o filme normal')
	escreva(c3, 'Pessoas Acharam o filme ótimo')
	
	


Questão 03



aluno=input('digite o nome do infeliz: ')

n1=float(input('Digite a 1ªNota(com ponto marcando as casas decimais): '))
n2=float(input('Digite a 2ªNota(com ponto marcando as casas decimais): '))
n3=float(input('Digite a 3ªNota(com ponto marcando as casas decimais): '))

calcula=(n1+n2+n3)/3

if calcula >= 7.00:
    print('O(a)',aluno,'teve média de: %.2f e está aprovado(a)' %calcula)

elif calcula >= 4.00 and calcula<7.00:
    print('O(a)',aluno,'teve média de: %.2f e está na prova final' %calcula)
else:
    print('O(a)',aluno,'teve média de: %.2f e está reprovado(a)' %calcula)
	
	
	
Questão 04