#can be any of the map
romaniaMap = {
    'Arad': ['Sibiu', 'Zerind','Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}
#code
from queue import Queue
def Bfs(source,destination):

    explored={}
    parent={}
    traversal_output=[]

    frontier=Queue()
    for city in romaniaMap.keys():
        explored[city]=False
        parent[city]=None
    
    explored[source]=True
    frontier.put(source)

    while not frontier.empty():
        current_city=frontier.get()
        

        for neighbour_city in romaniaMap[current_city]:
            if not explored[neighbour_city]:
                explored[neighbour_city]=True
                parent[neighbour_city]=current_city
                frontier.put(neighbour_city) 
 
    route=[]
    backtrack=destination
    while backtrack is not None:
        route.append(backtrack)
        backtrack=parent[backtrack]
    route.reverse()

    print(route)
                            
            

Bfs("Arad",'Bucharest')
    