import os;
os.system("cls");
print ("---------------- Programa Chinês ----------------");
# funcao para calcular parcelas com juros "def" = funcao :

def calcularParcelas():
    produto = input ("Produto: ");
    valor = float(input("Valor: "));
    parcelas =  int(input("Número de parcelas: "));
    juros = int(input("Juros mensal: "));
    # calcular parcelas
    valorParcela = valor / parcelas;
    total = 0;
    for i in range(1, parcelas + 1):
        if (i > 1):
            valorParcela = valorParcela + ( valorParcela * juros / 100); 
        
        total = total + valorParcela;
        print(f"Parcela {i}: R$ {valorParcela:.2f}");
    print (f"Valor total é de R$ {total:.2f}");
    print (f"----------------------------");
    resposta = input("Você deseja sair [S + Enter] ou continuar [Qualquer Teclad + Enter]?");
    if (resposta == "S"):
        print("Tchauzinho");
    else: 
        calcularParcelas();

calcularParcelas();