from collections import deque
import heapq

# Busca em profundidade recursiva. Escolhe um vizinho e vai até o fim dele. Não garante o melhor caminho e sim o "primeiro" que ele encontra.
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

    caminho.pop()
    return None

# Busca em largura com fila. Realiza a busca em camadas, encontrando o caminho que visite menos nós. Não garante o melhor caminho pois considera a quantidade de nós e não o peso das arestas.
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


# Usa fila de prioridade (heapq) e sempre expande o vizinho com a aresta de menor peso, sem reconsiderar. Por ser um algoritmo guloso ele faz sempre a melhor decisão local não garantindo a melhor solução global.
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


# Acha o caminho de menor custo total. Mantém a menor distância conhecida até cada porta e sempre finaliza a porta de menor distância (heapq).Se achar um caminho melhor para um vizinho, atualiza distancia e anterior.
def dijkstra(grafo, origem, destino):
    distancia = {p: float("inf") for p in grafo}
    anterior = {}
    distancia[origem] = 0
    fila = [(0, origem)]
    finalizadas = set()

    while fila:
        d, atual = heapq.heappop(fila)
        if atual in finalizadas:
            continue
        finalizadas.add(atual)

        if atual == destino:
            break

        for vizinho, peso in grafo[atual]:
            if vizinho in finalizadas:
                continue
            nova = d + peso
            if nova < distancia[vizinho]:
                distancia[vizinho] = nova
                anterior[vizinho] = atual
                heapq.heappush(fila, (nova, vizinho))


    if distancia[destino] == float("inf"):
        return [], float("inf"), len(finalizadas)

    caminho = [destino]
    while caminho[-1] != origem:
        caminho.append(anterior[caminho[-1]])
    caminho.reverse()

    return caminho, distancia[destino], len(finalizadas)
