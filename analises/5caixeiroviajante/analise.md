[<img src="../../img/assets/back.png" height="35px" style="position: fixed; top: 15; opacity: 0.45">](../../README.md)

# <div align="center">Análise 5: Caixeiro-viajante</div>

## Análise Linha-a-Linha

<details>

   <summary style="color: lightgray">
        Clique aqui para ver a análise linha-por-linha
    </summary>

| Linha | Código                                                                                                                                                                                                                   | Espaço | Vezes | Custo | Total |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------|-------|-------|
| 1     | `CaixeiroViajanteForcaBruta(Cidades)`                                                                                                                                                                                    |      n |     1 |    c1 | c1 |
| 2     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`n <- tamanho de Cidades`                                                                                                                                                |      n |     1 |    c2 | c2 |
| 3     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Permutações <- gerar todas as permutações possíveis de cidades`                                                                                                         |     n! |     1 |    c3 | c3 * n! |
| 4     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MelhorRota <- null`                                                                                                                                                     |     c4 |     1 |    c4 | c4 |
| 5     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MenorDistância <- infinito`                                                                                                                                             |     c5 |     1 |    c5 | c5     |
| 6     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`para cada rota em permutações`                                                                                                                                          |     c6 | n! + 1 |   c6 | c6 * (n! + 1)      |
| 7     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DistânciaAtual <- 0`                                                                                                    |     c7 |    n! |    c7 | c7 * (n!)      |
| 8     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`para i <- 1 até n - 1`                                                                                                  |     c8 | (n! * n) |    c8 | c8 * (n! * n)      |
| 9     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DistânciaAtual <- DistânciaAtual + distância entre Rota[i] e Rota[i+1]` |     c9 |    n! |    c9 | n! * c9      |
| 10    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DistânciaAtual <- DistânciaAtual + distancia entre Rota[n] e Rota[1]`                                                   |    c10 |    n! |   c10 | n! * c10      |
| 11    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`se DistânciaAtual < MenorDistância`                                                                                     |    c11 |    n! |   c11 | n! * c11      |
| 12    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MenorDistancia <- DistânciaAtual`                                       |    c12 |    n! |   c12 | n! * c12      |
| 13    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MelhorRota <- Rota`                                                     |    c13 |    n! |   c13 | n! * c13      |
| 14    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`retornar MelhorRota, MenorDistância`                                                                                                                                    |    c14 |     1 |   c14 | c14      |
|       |                                                                                                                                                                                                                          |        |       |       | c1 + c14 + c2 + c4 + c5 + c6 + (c10 + c11 + c12 + c13 + c3 + c6 + c7 + c9 + c8 n) n! |
|       |                                                                                                                                                                                                                          | ~θ(n!) |       |       | ~θ(n!) (espaço e tempo) |

</details>
