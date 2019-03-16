import string 
import datetime 
import re 
import itertools 
import math 
import collections 

class Graph(object): 
    def __init__(self, graph, start='a'): 
        self.graph = graph 
        self.unvisited = ' '.join(string.ascii_letters[0:6]).split()
        self.visited = collections.deque()  
        self.prev = str() 
        self.shortest_distance_from_start = [math.inf] * len(graph[0]) 
        self.neighbours = dict() 


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
        vrtices = ' '.join(string.ascii_letters[0:6]).split()
        for r in enumerate(vrtices): # note r[1] s a tuple 
            for c in enumerate(vrtices): # note c[1] s a tuple 
                if (self.graph[r[0]][c[0]] == 0): 
                    continue 
                if r[1] in self.neighbours.keys(): 
                    self.neighbours[r[1]].append(c[1]) 
                else :
                    self.neighbours[r[1]] = list() 
                    self.neighbours[r[1]].append(c[1]) 

        print(self.neighbours)
 
def main(): 
    

    graph = [
           [0, 7, 9, 0, 0, 14],
           [0, 0, 10, 15, 0, 0],
           [0, 0, 0, 11, 0, 2],
           [0, 0, 0, 0, 6, 0],
           [0, 0, 0, 0, 0, 9],
           [0, 0, 0, 0, 0, 0]] 

    g = Graph(graph) 
    g.prnt() 
    g.dijkstra() 



if __name__ == '__main__': 
    main() 
    ''' 
    graph = [
             #a  b  c  d  e  f 
           a [0, 7, 9, 0, 0, 14], 
           b [7, 0, 10, 15, 0, 0], 
           c [9, 10, 0, 0, 0, 2], 
           d [0, 15, 0, 0, 6, 0],
           e [0, 0, 0, 6, 0, 9],
           f [14, 0, 2, 0, 9, 0]]

    ''' 
