from buscas import bfs, busca_dfs, dfs, gulosa
from tabulate import tabulate
import textwrap

def carregar_grafo(caminho):
    grafo = {}
    with open(caminho, encoding="utf-8") as arq:
        for linha in arq:
            if not linha.strip():
                continue
            a, b, peso = linha.split()
            peso = int(peso)
            grafo.setdefault(a, []).append((b, peso))
            grafo.setdefault(b, []).append((a, peso))
    return grafo

def imprimir_grafo(grafo):
    for origem in sorted(grafo.keys()):
        vizinhos = grafo[origem]
        print(f"{origem} -> {vizinhos}")

def main():
    grafo = carregar_grafo("arestas.txt")

    funcoes = [('DFS', dfs(grafo, 'Tech', 'Patio_1')), ('BFS', bfs(grafo, 'Tech', 'Patio_1')), ('Gulosa', gulosa(grafo, 'Tech', 'Patio_1'))]

    resultados_tabela = []

    for nome_algoritmo, resultado in funcoes:
        if resultado is not None:
            caminho, custo, casas_visitadas = resultado
            
            caminho_str = " -> ".join(caminho)
            
            caminho_formatado = textwrap.fill(caminho_str, width=50)
            
            resultados_tabela.append([nome_algoritmo, caminho_formatado, custo, casas_visitadas])
        else:
            resultados_tabela.append([nome_algoritmo, "Caminho não encontrado", "-", "-"])

    cabecalhos = ["Algoritmo", "Caminho", "Custo Total", "Nós Visitados"]
    tabela = tabulate(resultados_tabela, headers=cabecalhos, tablefmt="grid")
    
    print(tabela)

if __name__ == "__main__":
    
    main()
    