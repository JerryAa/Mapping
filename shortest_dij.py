import string 
import datetime 
import re 
import itertools 
import math 
import collections 

class Graph(object): 
    def __init__(self, graph, start='a'): 
        self.graph = graph 
        self.vertices = ' '.join(string.ascii_letters[0:6]).split()
        self.unvisited = dict(zip(self.vertices, range(7))) 
        self.visited = collections.deque()  
        self.prev = dict() 
        self.neighbors = dict() 
        self.start = start 
        self.distance = dict(zip(self.vertices, [math.inf] * len(self.vertices)))

    def prnt (self): 
        ''' 
        print adjacency matrix 
        '''
        for r in self.graph: 
            for c in r: 
                print(f'{c}', end=" ") 
            print("\n") 

        return True 
            
    def dijkstra(self): 

        for r in enumerate(self.vertices): # note r[1] s a tuple 
            for c in enumerate(self.vertices): # note c[1] s a tuple 
                if (self.graph[r[0]][c[0]] == 0): # no connection 
                    continue 
                if r[1] in self.neighbors.keys(): 
                    self.neighbors[r[1]].append((c[1], self.graph[r[0]][c[0]])) 
                else :
                    self.neighbors[r[1]] = list() 
                    self.neighbors[r[1]].append((c[1], self.graph[r[0]][c[0]])) 


        for vertex in self.vertices: 
            self.distance[vertex] = math.inf
            self.visited.append(vertex) 
            self.prev[vertex] = None 

        self.distance[self.start] = 0 
        
        while self.visited:
            u = min(self.visited, key=lambda vertex: self.distance[vertex])
            if (u in self.visited):
                self.visited.remove(u)

            if self.distance[u] == math.inf:
                break
                 

            try: 
                for neighbor in self.neighbors[u]:
                    alt = self.distance[u] + neighbor[1]
                    v = neighbor[0]

                    if alt < self.distance[v]:
                        self.distance[v] = alt
                        self.prev[v] =u
         
            except KeyError: 
                continue 

        print(f'Distance: {self.distance}')
         
        return self.distance 
         
def main(): 
    graph = [
           [0, 7, 9, 0, 0, 14],
           [0, 0, 10, 15, 0, 0],
           [0, 0, 0, 11, 0, 2],
           [0, 0, 0, 0, 6, 0],
           [0, 0, 0, 0, 0, 9],
           [0, 0, 0, 0, 0, 0]] 

    g = Graph(graph) 
    g.dijkstra() 



if __name__ == '__main__': 
    main() 
    ''' 
    graph = [
             a  b  c  d  e  f 
          a [0, 7, 9, 0, 0, 14],
          b [0, 0, 10, 15, 0, 0],
          c [0, 0, 0, 11, 0, 2],
          d [0, 0, 0, 0, 6, 0],
          e [0, 0, 0, 0, 0, 9],
          f [0, 0, 0, 0, 0, 0]] 

    ''' 
