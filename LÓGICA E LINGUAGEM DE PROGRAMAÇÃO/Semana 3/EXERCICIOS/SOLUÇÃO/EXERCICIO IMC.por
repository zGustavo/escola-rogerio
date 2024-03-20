programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real peso, altura, imc, arredondamento

    escreva("Informe seu peso: ")
    leia(peso)
    escreva("Informe sua altura: ")
    leia(altura)

    imc = peso / (altura * altura)
    arredondamento = mat.arredondar(imc, 3)

    se(imc < 17) {
      escreva("MUITO ABAIXO DO PESO SEU IMC É: ", arredondamento)
    }senao se(imc >= 17 e imc < 18.5) {
      escreva("ABAIXO DO PESO SEU IMC É: ", arredondamento)
    }senao se(imc >= 18.5 e imc < 25) {
      escreva("PESO NORMAL SEU IMC É: ", arredondamento)
    }senao se(imc >= 25 e imc < 30) {
      escreva("ACIMA DO PESO SEU IMC É: ", arredondamento)
    }senao se(imc >= 30 e imc < 35) {
      escreva("OBESIDADE 1 SEU IMC É: ", arredondamento)
    }senao se(imc >= 35 e imc < 40) {
      escreva("OBESIDADE 2 SEU IMC É: ", arredondamento)
    }senao {
      escreva("OBESIDADE 3 SEU IMC É: ", arredondamento)
    }
  }
}
