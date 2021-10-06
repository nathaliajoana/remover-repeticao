# letras.py - Mini-teste de programação | letras.mus.br

## Função
Essa aplicação tem como função remover duplicação do fim de cada palavra de um texto, mas somente se todas as palavras do texto forem duplicadas. O texto de saída receberá um ponto final.

## Como usar
* O projeto é adaptado para Python2 e Python3.
* Clone o repositório e abra o arquivo em seu IDE de preferência.
* Digite o comando no terminal:
> python letras.py
* Insira então sua entrada:
> sua entrada aqui
* O texto final será imprimido.

## Entrada >> Saída
### Casos-teste: textos de uma linha com pelo menos uma palavra, em letras minúsculas, sem caracteres especiais e sem acentuação, com palavras separadas por apenas um caractere de espaço.
- oo ratoato roeuoeu aa roupaoupa dodo reiei dee romaoma >> **o rato roeu a roupa do rei de roma.**
- banana >> **bana.**
- a bananeira tem banana >> **a bananeira tem banana.**

## Algoritmo
- A string de entrada é separada em um array de palavras.
- Para cada palavra no array, é feita uma requisição para a função busca_repeticao().
- Na função busca_repeticao(), para palavras:
    1. De dois caracteres -> é verificada a repetição do primeiro caractere.
    2. De tamanho par -> é verificada a repetição em pares de caracteres, a partir do último.
    3. De tamanho ímpar -> é desconsiderado o primeiro caractere e são comparados os subsequentes.
- Um contador ("changes") verifica a quantidade de mudanças feitas e, se todas as palavras tiverem repetições, é retornada a nova frase, sem duplicações.
- Caso contrário, é retornada a frase original, pois nem todas as palavras são duplicadas.
- Finalmente, a resposta é imprimida com a adição de um ponto final.

## Autora
* **Nathália Joana**: @nathaliajoana (https://github.com/nathaliajoana)
