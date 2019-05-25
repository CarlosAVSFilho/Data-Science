from igraph import Graph
from igraph import plot

grafo5 = Graph(edges = [(0,1), (2,3), (0,2), (0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo5.vs['peso'] = [40, 30, 30, 25]
grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo'] 
grafo5.es['weight'] = [1,2,1,3]

for v in grafo5.vs:
    print(v)
    
for e in grafo5.es:
    print(e)
    
grafo5.vs['cor'] = ['blue', 'red', 'yellow', 'green']

plot(grafo5, bbox = (250, 250), vertex_size = grafo5.vs['peso'],
                                vertex_color = grafo5.vs['cor'],
                                vertex_shape = 'square',
                                edge_width = grafo5.es['weight'],
                                edge_curved = 0.25)

#tkplot não disponível em python, somente em R.