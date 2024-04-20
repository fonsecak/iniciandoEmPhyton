import os;
os.system("cls");

# funcao para saber o valor das parcelas
def calcularParcela(produto, valor, parcelas):
    valor = float(valor);
    parcelas = int (parcelas);
    valorParcela = valor / parcelas;
    print (f"O valor das parcelas do produto {produto} são de R% {valorParcela:.2f}");
    

print ("---------------- Programa Chinês ----------------");
produto = input ("Digite o nome do produto: ");
valor = input ("Digite o valor do produto: ");
parcelas = input ("Digite as parcelas: ");

# chamar a função calcularParcela

calcularParcela (produto, valor, parcelas);