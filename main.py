peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))

imc = peso / (altura * altura)
print (imc)

if ( imc < 18.5):
    print ("Abaixo do peso")
elif (imc < 25):
    print ("peso normal")
elif (imc < 30):
    print ("sobrepeso")
elif (imc < 35):
    print ("obesidade grau 1")
elif (imc < 40):
    print ("obesidade grau 2")
else:
    print ("obesidade grau 3")


    



    
