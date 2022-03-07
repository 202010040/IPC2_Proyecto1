import graphviz
import os
import pydot
import tempfile

dot = graphviz.Digraph('round-table', comment='The Round Table') #Crear un dot
dot.node('A', 'King Arthur')  
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
dot.render(directory='doctest-output').replace('\\', '/')
graf = pydot.graph_from_dot_data(dot.source)
graf0 = (graf[0])
graf0.write