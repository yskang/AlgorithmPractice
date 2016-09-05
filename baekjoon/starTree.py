#                        *                        
#                       * *                       
#                      *****                      
#                     *     *                     
#                    * *   * *                    
#                   ***** *****                   
#                  *           *                  
#                 * *         * *                 
#                *****       *****                
#               *     *     *     *               
#              * *   * *   * *   * *              
#             ***** ***** ***** *****             
#            *                       *            
#           * *                     * *           
#          *****                   *****          
#         *     *                 *     *         
#        * *   * *               * *   * *        
#       ***** *****             ***** *****       
#      *           *           *           *      
#     * *         * *         * *         * *     
#    *****       *****       *****       *****    
#   *     *     *     *     *     *     *     *   
#  * *   * *   * *   * *   * *   * *   * *   * *  
# ***** ***** ***** ***** ***** ***** ***** *****

# n = int(input())
n = 30

def printTriangle(position, map):
    edges = []
    (x, y) = position
    map.set(x, y, '*')
    map.set(x-1, y+1, '*')
    map.set(x+1, y+1, '*')
    map.set(x-2, y+2, '*')
    map.set(x-1, y+2, '*')
    map.set(x, y+2, '*')
    map.set(x+1, y+2, '*')
    map.set(x+2, y+2, '*')
    if x-3 > 0 and x + 3 < map.w and y + 3 < map.h:
        edges.append((x-3, y+3))
        edges.append((x+3, y+3))
    return edges

class Map:
    def __init__(self, w, h, value):
        self.w = w
        self.h = h
        self.map = [[value for col in range(w)] for row in range(h)] 
    
    def set(self, x, y, value):
        self.map[y][x] = value
    
    def draw(self):
        for i in range(h):
            print(''.join(self.map[i]))

w = (int)((n/3)*5+(n/3-1))
h = n

map = Map(w, h, ' ')
start = n - 1 
nextPoints = printTriangle((start, 0), map)
while nextPoints:
    point = nextPoints.pop()
    tempPoints = printTriangle(point, map)
    for p in tempPoints:
        nextPoints.append(p)
    
map.draw()
        
