import math
# EXPLANATION
# we have used a nearest neighbor algorithm since we need to visit ervey tuple in the list and 
# get to the finishing point with also having 
#  a short path.here the problem is similar or asking such a solution which is given simply using nna, 
# thats why i have used this instead of bfs,dfs, or other.

#main fn
def optimize_route(destinations):
    if len(destinations) <= 1:
        return destinations
    
    
    start = destinations[0]
    other_points = destinations[1:]
    optimized_route = [start]
    unvisited = other_points.copy()
    current_point = start
    
    while unvisited:
        nearest_point = min(unvisited, 
                        key=lambda point: distance(current_point, point))
        # anonymous lamda fn to pick up opoint of smallest distance
        
        optimized_route.append(nearest_point)
        unvisited.remove(nearest_point)
        current_point = nearest_point
    
    return optimized_route

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(route):
    if len(route) <= 1:
        return 0
    
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    return total
