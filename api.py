from fastapi import FastAPI, HTTPException
from grafo import carregar_grafo
from buscas import bfs, dfs, gulosa, dijkstra

app = FastAPI()
grafo = carregar_grafo("arestas.txt")

@app.get("/vizinhos/{porta}")
def vizinhos(porta: str):
    if porta not in grafo:
        raise HTTPException(404, "Porta não encontrada")
    return [{"porta": p, "peso": w}
            for p, w in grafo[porta]]

@app.get("/portas")
def portas():
    return [porta for porta in grafo.keys()]

@app.get("/rota")
def rota(origem: str, destino: str, algoritmo: str):
    
    if origem not in grafo or destino not in grafo:
        raise HTTPException(404, "Origem ou destino não existem no mapa.")

    caminho = []
    custo = 0
    casas_visitadas = 0

    if algoritmo.lower() == "dfs":
        caminho, custo, casas_visitadas = dfs(grafo, origem, destino)
    elif algoritmo.lower() == "gulosa":
        caminho, custo, casas_visitadas = gulosa(grafo, origem, destino)
    elif algoritmo.lower() == "bfs":
        caminho, custo, casas_visitadas = bfs(grafo, origem, destino)
    elif algoritmo.lower() == "dijkstra":
        caminho, custo, casas_visitadas = dijkstra(grafo, origem, destino)

        
    return {
        "algoritmo": algoritmo,
        "caminho": caminho,
        "custo": custo,
        "unidade": "passos",
        "visitados": casas_visitadas
    }

@app.get("/comparar")
def comparar(origem: str, destino: str):
    if origem not in grafo or destino not in grafo:
        raise HTTPException(404, "Origem ou destino não existem no mapa.")

    algoritmos = {
        "DFS": dfs,
        "BFS": bfs,
        "Gulosa": gulosa,
        "Dijkstra": dijkstra
    }

    resultados = []

    for nome, funcao in algoritmos.items():
        caminho, custo, casas_visitadas = funcao(grafo, origem, destino)
        
        resultados.append({
            "algoritmo": nome,
            "caminho": caminho,
            "custo": custo,
            "visitados": casas_visitadas
        })

    return resultados