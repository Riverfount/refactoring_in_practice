"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().
"""

import sys
from collections import Counter


def parse_file(file) -> Counter:
    with open("letras.txt", "r") as file:
        for line in list(file.readlines()):
            line_parsed = Counter([l.lower() for l in line])
            del line_parsed[" "]
    return line_parsed


def print_words(filename):
    line_parsed = parse_file(filename)
    for word in sorted(line_parsed.keys()):
        print(f"{word} {line_parsed[word]}")


def print_top(filename):
    line_parsed = parse_file(filename)
    line_parsed_ordered = {
        k: v
        for k, v in sorted(line_parsed.items(), key=lambda item: item[1], reverse=True)
    }
    for word in line_parsed_ordered:
        print(f"{word} {line_parsed_ordered[word]}")


# A função abaixo chama print_words() ou print_top() de acordo com os parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print("Utilização: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == "__main__":
    main()
