# importar pacote do SO Sistema Operacional
import os
# limpar a tela
os.system("cls");

salario = input ("Digite seu salario: ");
aumento = input ("Digite a % do seu aumento: ");
salario = float(salario);
aumento = float(aumento);
novoSalario = salario + (salario * aumento /100);
print (f"O novo salário é R$ {novoSalario:.2f}");
