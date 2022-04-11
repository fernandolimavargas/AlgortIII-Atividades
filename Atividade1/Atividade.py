'''To Do List : 

Desenvolva uma To Do List (Lista de Tarefas) em Python utilizando, obrigatoriamente, listas encadeadas (livre escolha de qual delas será a mais adequada). 

Como será essa aplicação? 

- Deve contemplar todas principais atividades de um CRUD simples, isto é: Inserir, Deleter, Remover e Alterar - uma tarefa ou várias. 

- Implementar um pequeno menu dando a opção de escolha ao usuário e, consequentemente, viabilizando maior interação com a aplicação. 

- Além das operações básicas também podem implementar outras funcionalidades, como por exemplo, marcar uma tarefa como feita e manter ela destacada na listagem (ou não). 

Dicas: 

- Procure modularizar a sua aplicação o máximo que conseguir, mantendo coesão e coerência do início ao fim. Não esquecendo dos quatro pilares da Programação Orientada a Objetos

- Use a criatividade, destaquei pontos essenciais apenas. 

Observação: o objetivo dessa atividade é o meu primeiro contato com a prática de vocês, isto é, não está vinculada a um conceito de forma direta. As observações obtidas com as entregas serão fundamentais para que possamos começar e permanecer da maneira mais alinhada possível, o que é muito importante nessa modalidade. 

- O que você envia? Um zip com um código, um txt com link do Git.... 

Dúvidas? Escrevam um e-mail :D

Att,

Eduarda'''

from EasterEgg import * 


def fazer_pedido(): 
    escolha = EasterEgg(0, 0, 0)
    escolha.reaDate()
    print (f'''Seu pedido ficou: 
    Casca: {escolha.casca}
    Tamanho: {escolha.tamanho}
    Recheio: {escolha.recheio}''')
    PEDIDO_CASCA.append(escolha.casca)
    PEDIDO_TAMANHO.append(escolha.tamanho)
    PEDIDO_RECHEIO.append(escolha.recheio)
    imprimir()

def excluir_pedido(): 
    id = int(input('Qual pedido que você deseja cancelar? '))
    del PEDIDO_CASCA[id]
    del PEDIDO_TAMANHO[id]
    del PEDIDO_RECHEIO[id]


def alterar_produto():
    mod = input('Qual item você deseja modificar? ')
    if mod in PEDIDO: 
        prod_mod = input('Produto novo: ') 
        PEDIDO[mod] = prod_mod
    else: 
        input('Produto não cadastrado. [ENTER] Para continuar.')
        

def imprimir(): 
    print(f'CASCA      {PEDIDO_CASCA}')
    print(f'TAMANHO    {PEDIDO_TAMANHO}')
    print(f'Recheio    {PEDIDO_RECHEIO}')


while True: 
    menu = input (''' Menu: 
    0 - Parar programa
    1 - Fazer pedido
    2 - Excluir Pedido
    3 - Alterar Pedido
    4 - Imprimir Pedido

    Opção:''')

    if menu == '0':
        break

    if menu == '1':
        fazer_pedido()

    if menu == '2': 
        excluir_pedido()

    if menu == '3': 
        alterar_produto()

    if menu == '4':
        imprimir()