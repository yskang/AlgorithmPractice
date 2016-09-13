# Print Star - 11
# https://www.acmicpc.net/problem/2448

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
n = int(input())
w = n * 2 - 1
h = n

def unit(map, position):
    (x, y) = position
    map.set(x, y, '*')
    map.set(x-1, y+1, '*')
    map.set(x+1, y+1, '*')
    map.set(x-2, y+2, '*')
    map.set(x-1, y+2, '*')
    map.set(x, y+2, '*')
    map.set(x+1, y+2, '*')
    map.set(x+2, y+2, '*')

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

def drawTriangle(map, w, h):
    y = h - 1
    for x in range(h):
        map.set(x, y, '*')
        map.set(x, h-1, '*')
        y = y - 1

    for x in range(h-2, h+x):
        map.set(x, y, '*')
        map.set(x, h-1, '*')
        y = y + 1
    
def drawDivide(map, w, h, startPoint):
    if w == 5:
        return

    results = []
    (offsetX, offsetY) = startPoint
    width = int((w+1)/3)
    middleY = int(h / 2) - 1 

    for x in range(middleY + 2, w - middleY - 2):
        map.set(x+offsetX, middleY+offsetY, '*')
    
    x = middleY + 1
    for y in range(middleY+2, h-1):
        map.set(x+offsetX, y+offsetY, '*')
        map.set(w-x-1+offsetX, y+offsetY, '*')
        x = x + 1

    map.set(int(w/2)+offsetX, h-1+offsetY, ' ')

    drawDivide(map, int((w-1)/2), int(h/2), (middleY + 1 + offsetX, offsetY))
    drawDivide(map, int((w-1)/2), int(h/2), (offsetX, middleY+offsetY+1))
    drawDivide(map, int((w-1)/2), int(h/2), (int((w-1)/2+1)+offsetX, middleY+offsetY+1))
    

map = Map(w, h, ' ')
drawTriangle(map, w, h)
drawDivide(map, w, h, (0, 0))
map.draw()

