from collections import deque
import heapq

def dfs(grafo, inicio, saida):
    visitados = set()
    caminho = []
    custo = 0

    return busca_dfs(grafo, inicio, saida, visitados, caminho, 0)

def busca_dfs(grafo, atual, saida, visitados: set, caminho: list, custo):
    caminho.append(atual)
    visitados.add(atual)

    if atual == saida:
        return caminho, len(visitados)

    for nome, peso in grafo[atual]:
        if nome not in visitados:
            resultado = busca_dfs(grafo, nome, saida, visitados, caminho, custo + peso)

            if resultado is not None:
                return resultado, custo, len(visitados)

def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([inicio])
    origem = {}
    caminho = []

    while fila:
        v = fila.popleft()
        if v == saida:
            caminho = []
            atual = saida
            custo = 0
            
            while atual != inicio:
                caminho.append(atual)  
                pai, peso = origem[atual]
                custo += peso  
                atual = pai  
                
            caminho.append(inicio)      
            caminho.reverse()       
            return caminho, custo, len(visitados)
        for nome, peso in grafo[v]:
            if nome not in visitados:
                visitados.add(nome)
                fila.append(nome)
                origem[nome] = (v, peso)
                
def gulosa(grafo, inicio, saida):
    visitados = {inicio}
    origem = {}
    fila = []
    heapq.heappush(fila, (distancia(inicio, saida), inicio))
    custo = inicio[1]

    while fila:
        num_distancia, v = heapq.heappop(fila)

        if v == saida:
            caminho = []
            atual = saida
                    
            while atual != inicio:
                caminho.append(atual)    
                atual = origem[atual]   
                        
            caminho.append(inicio)      
            caminho.reverse()       
            return caminho, custo, len(visitados)
        
        for w in grafo[v]:
            if w[0] not in visitados:
                visitados.add(w)
                custo += w[1]
                heapq.heappush(fila, (distancia(w, saida), w))
                origem[w] = v

def distancia(atual, saida):
    return abs(atual[0] - saida[0]) + abs(atual[1] - saida[1])