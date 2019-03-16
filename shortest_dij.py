import string 
import datetime 
import re 
import itertools 

class Graph(object): 
    def __init__(self, graph): 
        self.graph = graph 
        unvisited = ' '.join(string.ascii_letters[0:6]).split()
        visited = [] 


    def prnt (self): 
        ''' 
        print adjacency matrix 
        '''
        for r in range(0, len(self.graph)): 
            for c in range(0, len(self.graph[0])): 
                print(f'{self.graph[r][c]} ', end=" ")
            print("\n") 

        return True 
            
 
def main(): 
    

    graph = [
            [0, 7, 9, 0, 0, 14], 
            [7, 0, 10, 15, 0, 0], 
            [9, 10, 0, 0, 0, 2], 
            [0, 15, 0, 0, 6, 0],
            [0, 0, 0, 6, 0, 9],
            [14, 0, 2, 0, 9, 0]]

    g = Graph(graph) 
    print(g.prnt()) 



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
