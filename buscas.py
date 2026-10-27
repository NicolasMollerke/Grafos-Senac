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
        return caminho, custo, len(visitados)

    for nome, peso in grafo[atual]:
        if nome not in visitados:
            resultado = busca_dfs(grafo, nome, saida, visitados, caminho, custo + peso)

            if resultado is not None:
                return resultado

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
    heapq.heappush(fila, (0, inicio))   

    while fila:
        num_distancia, v = heapq.heappop(fila)

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
                heapq.heappush(fila, (peso, nome))
                origem[nome] = (v, peso)
