programa {
  funcao inicio() {
    inteiro idade
    real peso
    logico tatuagem, alcool

    escreva("Qual sua idade: ")
    leia(idade)

    se(idade < 19 ou idade > 69) {
      escreva("Infelizmente, voc� n�o pode ser doador.")
    } senao {
      escreva("Qual seu peso: ")
      leia(peso)
      se(peso < 50) {
        escreva("Infelizmente, voc� n�o pode ser doador.")
      } senao {
        escreva("Voc� fez alguma tatuagem no �ltimo ano? (verdadeiro ou falso): ")
        leia(tatuagem)
        se(tatuagem == verdadeiro) {
          escreva("Infelizmente, voc� n�o pode ser doador.")
        } senao {
          escreva("Voc� ingeriu �lcool nas �ltimas 12 horas? (verdadeiro ou falso): ")
          leia(alcool)
          se(alcool == verdadeiro) {
            escreva("Infelizmente, voc� n�o pode ser doador.")
          } senao {
            escreva("Parab�ns, voc� pode doar sangue.")
          }
        }
      }
    }
  }
}
