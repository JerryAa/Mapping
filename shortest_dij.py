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
        self.prev = str() 
        self.neighbours = dict() 
        self.start = start 

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
                if r[1] in self.neighbours.keys(): 
                    self.neighbours[r[1]].append((c[1], self.graph[r[0]][c[0]])) 
                else :
                    self.neighbours[r[1]] = list() 
                    self.neighbours[r[1]].append((c[1], self.graph[r[0]][c[0]])) 
                     
        path = list() # path when you traverse min distance of each node 
        self.shortest_distance_from_start = dict(zip(self.vertices, [math.inf] * len(self.vertices)))

        self.shortest_distance_from_start[self.start] = 0 

        while True: 
            try: 
                smallest_dist = min(self.neighbours[self.start], key=lambda x: x[1]) 
                path.append(self.start)  
                self.start = smallest_dist[0] 
                self.visited.append(self.start) 
            except KeyError: # dead end 
                path.append(self.start)  
                break 
                 
        print(path) 
        print(self.shortest_distance_from_start) 
 
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
