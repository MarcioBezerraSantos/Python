# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para interpretar o IMC
def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Solicita os dados do usuário
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {interpretar_imc(imc)}")

## Atualizado Calculo IMC.