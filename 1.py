from buscas import bfs, busca_dfs, dfs, gulosa

def main():
    grafo = {
        'Tech': [('201', 5), ('Patio 1', 12)],
        '201': [('Tech', 5), ('202', 7)],
        'Patio 1': [('Tech', 12), ('Financeiro', 4), ('Lancheria 2', 5)],
        '202': [('201', 7), ('203', 12)],
        'Financeiro': [('Patio 1', 4), ('Saida', 9)],
        'Lancheria 2': [('Patio 1', 5), ('Predio Anexo', 36), ('Lancheria 1', 23)],
        '203': [('202', 12), ('Banheiro Feminino', 10)],
        'Saida': [('Financeiro', 9)],
        'Predio Anexo': [('Lancheria 2', 36), ('210', 4)],
        'Lancheria 1': [('Lancheria 2', 23), ('Patio 2', 10), ('Saida Biblioteca', 25)],
        'Banheiro Feminino': [('203', 10), ('Banheiro Masculino', 8), ('Patio 2', 3)],
        '210': [('Predio Anexo', 4), ('209', 4)],
        'Patio 2': [('Banheiro Feminino', 3), ('Lancheria 1', 10)],
        'Saida Biblioteca': [('Lancheria 1', 25), ('Biblioteca', 6), ('Estudos 2', 35)],
        'Banheiro Masculino': [('Banheiro Feminino', 8), ('Porta', 7)],
        '209': [('210', 4), ('Idiomas', 5)],
        'Biblioteca': [('Porta Biblioteca', 3), ('Saida Biblioteca', 6)],
        'Estudos 2': [('Saida Biblioteca', 35), ('Estudos 1', 4), ('Estudos 3', 1)],
        'Porta': [('Banheiro Masculino', 7), ('Secretaria', 3), ('204', 8)],
        'Idiomas': [('209', 5), ('208', 4), ('Nao Sei 2', 10)],
        'Porta Biblioteca': [('Biblioteca', 3), ('Professores', 2)],
        'Estudos 1': [('Estudos 2', 4)],
        'Estudos 3': [('Estudos 2', 1)],
        'Secretaria': [('Porta', 3), ('Administracao', 1)],
        '204': [('Porta', 8), ('Porta Salas', 5)],
        '208': [('Idiomas', 4)],
        'Nao Sei 2': [('Idiomas', 10), ('207', 9)],
        'Professores': [('Porta Biblioteca', 2), ('Diretoria', 6)],
        'Administracao': [('Secretaria', 1), ('Coordenacao', 1)],
        'Porta Salas': [('204', 5), ('205', 2)],
        '207': [('Nao Sei 2', 9), ('206', 10)],
        'Diretoria': [('Coordenacao', 3), ('Professores', 6)],
        '205': [('Porta Salas', 2), ('102', 19)],
        '206': [('207', 10), ('Saida Rua 1', 10)],
        'Coordenacao': [('Administracao', 1), ('Diretoria', 3)],
        '102': [('205', 19), ('Saida Rua 2', 1), ('Massagista', 5)],
        'Saida Rua 1': [('206', 10)],
        'Saida Rua 2': [('102', 1)],
        'Massagista': [('102', 5), ('Apoio Tecnico', 12)],
        'Apoio Tecnico': [('Massagista', 12), ('Copa', 5)],
        'Copa': [('Apoio Tecnico', 5), ('Rua', 2)],
        'Rua': [('Estetica', 5), ('Copa', 2)],
        'Estetica': [('Rua', 5)]
    }

if __name__ == "__main__":
    main()
    