# Navegação em Grafos no Senac - Algoritmos de Busca

Este projeto implementa uma API em Python utilizando FastAPI para calcular rotas dentro de um grafo que representa as portas do Campus do UniSenac. O sistema permite comparar o desempenho e os resultados de quatro algoritmos de busca de caminhos: DFS, BFS, Busca Gulosa e Dijkstra.

## Integrantes
* Nicolas Mollerke
* Ramiro Paz

## Unidade do Peso
O peso das arestas do nosso grafo representa o esforço ou a distância física entre os nós, sendo medido em **passos**. Um peso maior indica que duas salas estão mais distantes ou que a travessia exige mais tempo/esforço físico.

## Como Rodar o Projeto

Para executar a API localmente, siga o passo a passo abaixo no seu terminal:

**1. Crie o ambiente virtual:**
`python -m venv .venv`
*(No Windows, utilize `py -m venv .venv`)*

**2. Ative o ambiente virtual:**
* Windows: `.venv\Scripts\activate`
* Linux/Mac: `source .venv/bin/activate`

**3. Instale as dependências necessárias:**
`pip install fastapi uvicorn tabulate`

**4. Execute o arquivo grafo.py:**
`python grafo.py`

**5. Inicie o servidor FastAPI:**
`uvicorn api:app --reload`

**6. Teste as rotas no navegador ou em ferramentas como Insomnia/Postman:**
* Exemplo de busca de rota comparativa: `http://localhost:8000/comparar?origem=Tech&destino=Saida_Rua_2`

---

## Divergência entre Algoritmos: BFS vs Dijkstra

Durante os testes no grafo da estrutura, identificamos um cenário perfeito para ilustrar a diferença lógica entre a **Busca em Largura (BFS)** e o **Algoritmo de Dijkstra**.

**Cenário de Teste:**
* **Origem:** `Tech`
* **Destino:** `Patio_2`

### Por que eles discordam?
O **BFS** não leva os pesos das arestas em consideração. Seu único objetivo é encontrar o caminho que atravessa o **menor número de portas (arestas)** possível, ignorando o tamanho do corredor.
Já o **Dijkstra** ignora a quantidade de portas e foca exclusivamente em encontrar a rota com o **menor custo total (soma dos pesos)**. 

### O Caminho do BFS (Menos Saltos, Maior Custo)
Opta por ir pelo corredor das lancherias por exigir a travessia de apenas 4 portas. No entanto, ele cai na armadilha do corredor longo entre a `Lancheria_2` e a `Lancheria_1` (peso 23).
  * **Rota:** `Tech` → `Patio_1` → `Lancheria_2` → `Lancheria_1` → `Patio_2`
  * **Custo Total:** 50 passos (4 arestas)

### O Caminho do Dijkstra (Mais Saltos, Menor Custo)
Opta por passar pelo corredor das salas 200 e pelos banheiros. Mesmo precisando abrir uma porta a mais, ele calcula que o esforço físico total pelas salas de aula é consideravelmente menor.
  * **Rota:** `Tech` → `201` → `202` → `203` → `Banheiro_Feminino` → `Patio_2`
  * **Custo Total:** 37 passos (5 arestas)

Isso prova que, em mapas com distâncias irregulares, o caminho com menos transições não é necessariamente o caminho mais curto fisicamente.