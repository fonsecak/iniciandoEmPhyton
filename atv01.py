import os;
os.system ("cls");

print ("--------------- Calcular média ---------------")

def calcularMedia ():
    disciplina = input ("Disciplina: ");
    notaUm = float(input("Nota 1° Bimestre: "));
    notaDois = float(input("Nota 2° Bimestre: "));

    mediaNotas = (notaUm + notaDois ) /2 ;
    
    if (mediaNotas >= 7 ):
        print(f"Sua média é {mediaNotas:.1f} você PASSOU na disciplina de {disciplina} MLK");
    else :
         print(f"Sua média é {mediaNotas:.1f} você Foi mlk demais F!!!! na disciplina de {disciplina}");
    
    resposta = input ("Deseja sair [S + Enter] caso queira continuar calculando [Qualquer tecla + Enter]" );

    if (resposta == "S"):
        calcularMedia();
    else: 
        print ("tchau");

calcularMedia ();
    