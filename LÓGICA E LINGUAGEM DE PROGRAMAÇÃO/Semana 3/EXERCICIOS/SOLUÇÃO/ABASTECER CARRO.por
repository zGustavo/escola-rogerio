programa {
  funcao inicio() {
    real kmlitro, combustivelNoCarro, distancia, precisaAbastecer    

    escreva("QUANTOS KM O CARA FAZ POR LITRO: ")
    leia(kmlitro)
    escreva("QUANTOS LITRO DE GASOLINA AINDA TEM NO CARRO? ")
    leia(combustivelNoCarro)
    escreva("QUAL A DISTANCIA VOC� DESEJA PERCORRER? ")
    leia(distancia)

    se(combustivelNoCarro > 0) {
      precisaAbastecer = (kmlitro * combustivelNoCarro)
      precisaAbastecer = (precisaAbastecer - distancia)
      se(precisaAbastecer < 0) {
        precisaAbastecer = precisaAbastecer * -1
        precisaAbastecer = precisaAbastecer / kmlitro
        escreva("Voc� precisa abastecer ", precisaAbastecer, " litros")
      } senao {
        escreva("Voc� n�o precisa abastecer")
      }

    } senao {
      precisaAbastecer = distancia / kmlitro
      escreva("Voc� precisa abastecer ", precisaAbastecer, " litros")
    }
  }
}
