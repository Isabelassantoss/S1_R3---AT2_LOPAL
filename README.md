# AT2 - exercícios de programação em python 🧑‍💻

## Projeto 🔎
Essa atividade tem como objetivo: Resolução de problemas com racíocinio lógico,
construção de passo a passos para realizar alguma tarefa.

## Atividade 1
<img width="460" height="359" alt="image" src="https://github.com/user-attachments/assets/72f7689f-2b87-4f88-ba04-6348aeb5581d" />

Seu objetivo é mostrar quais numeros de 1 a 100 são ipares ou pares. primeiro ele cria uma fila de números que começa no 0 e vai até o 100. O código vai pegar um por um dessa fila para testar. depois é usado o *if numero % 2 == 0* ele é o teste matemático, ele divide o número atual por 2, se o resto da divisão for zero significa que o número é par por ultimo os "prints" que mostram as respostas dizendo se é um número impar ou par.

## Atividade 2
<img width="586" height="423" alt="image" src="https://github.com/user-attachments/assets/10a57a97-c949-4a66-b2fa-a782c37de0b2" />

Este código encontra o maior e o menor de três números.Primeiro, ele recebe esses três números. Depois, armazena esses valores em uma lista. As funções max() e min() encontram os extremos.

## Atividade 3
<img width="428" height="442" alt="image" src="https://github.com/user-attachments/assets/dd555627-a6b7-4166-b5df-211dda226a99" />

O programa recebe um nome inicia um contador em 1. Em seguida, ele anda por cada letra do nome usando um laço *for*. A cada iteração, o código usa fatiamento *([0:quantidade])* para mostrar o texto do início até a posição atual e aumenta o contador em 1 para  mostrar a próxima letra na linha seguinte.

## Atividade 4
<img width="937" height="320" alt="image" src="https://github.com/user-attachments/assets/e27525f8-c7e9-49d1-9881-3edfe1e8d91e" />

É pedido ao usuário o número de elementos desejados. Assim um laço for roda o número de vezes solicitado, adicionando o valor atual à lista serie e atualizando os próximos números com a soma dos dois anteriores. No final, o operador * desempacota a lista para exibir os números separados por espaços.

## Atividade 5
<img width="737" height="845" alt="image" src="https://github.com/user-attachments/assets/5365ab6e-033e-4c24-9d2d-12275728d8e0" />

O programa solicita cinco informações (nome, idade, salário, sexo e estado civil). Caso o usuário digite um valor inválido o laço while exibe uma mensagem de erro e exige uma nova digitação até que o dado seja correto. No final, exibe uma mensagem de sucesso.

## Atividade 6
<img width="548" height="318" alt="image" src="https://github.com/user-attachments/assets/6acd4a52-6a1a-433f-9826-a55f4ea26bb6" />

Primeiro o codigo descarta números menores que 2, os numeros que sobram ele usa um laço *for* para tentar dividi-los por todos os valores entre 2 e o próprio número. De pois ele usa (% == 0), o código identifica se o número é divisível por outro, exibe que não é primo e interrompe com o break. Caso o laço termine sem o break, a estrutura *else* é executada, confirmando que o número é primo.

## Atividade 7 
<img width="555" height="299" alt="image" src="https://github.com/user-attachments/assets/90838649-3956-4fea-97ce-574c1e82d270" />

Este código calcula e exibe o fatorial de um número dado pelo usuário.O programa inicializa a variável fatorial com o valor 1. Em seguida, um laço for percorre todos os números de 1 até o valor digitado. A cada repetição, o código multiplica o valor pelo número atual da contagem (i). Ao final de todas as multiplicações, uma f-string exibe o resultado total na tela.

## Atividade 8 
<img width="751" height="322" alt="image" src="https://github.com/user-attachments/assets/9345a4ad-d1e7-471d-b590-737e805ec792" />

A partir de uma lista com sete números, o programa calcula e exibe de forma direta o total de elementos com len(), o maior valor com max(), o menor valor com min() e a soma de todos os itens com sum(). Por ultimo, ele utiliza a função sorted() para gerar e exibir novas versões dessa lista organizadas tanto em ordem crescente quanto em ordem decrescente (usando reverse=True).

## Atividade 9 
<img width="758" height="272" alt="image" src="https://github.com/user-attachments/assets/93506474-da82-4a84-b3b7-621c2bca9340" />

Ele demostra a criação e a exibição de um dicionário em Python para estruturar os produtos e preços de uma lanchonete.O programa armazena os nomes dos alimentos como chaves (strings) e associa a cada um deles o seu respectivo valor (números decimais).

## Atividade 10
<img width="478" height="308" alt="image" src="https://github.com/user-attachments/assets/eecf0e1d-5835-4e0c-9c84-c3ebfeac1a09" />

É armazenado uma senha padrão em formato de texto e solicita a tentativa do usuário. Um laço while compara o dado inserido com a senha armazenada; caso sejam diferentes (!=), o código exibe uma mensagem de erro e pede uma nova senha.

## Atividade 11
<img width="693" height="636" alt="image" src="https://github.com/user-attachments/assets/6d6cd4ef-a73c-4bd2-a00e-3881e8586c27" />

O código gera e exibe de a tabuada de um número escolhido pelo usuário.O programa recebe um número inteiro e monta o cabeçalho usando quebras de linha *(\n)* e linhas divisórias feitas com a repetição de traços ("-" * 13). Em seguida, um laço *for* percorre os multiplicadores de 1 a 10 (range(1, 11)).
