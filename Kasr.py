class kasr:
    
    def _init_(Temp, x=None, y=None):

        Temp.x = x
        Temp.y = y


    def Show(Temp):

        return str(Temp.x) + '/' + str(Temp.y)
    
     
    
    
    def Sum(Temp, second):
        
        result = kasr()
        result.x = Temp.x*second.y + Temp.y*second.x
        result.y = Temp.y*second.y
        return result
    
    
    
    
    def Multiple(Temp, second):
        
        result = kasr()
        result.x = Temp.x*second.x
        result.y = Temp.y*second.y
        return result
    
    
    
    
    def Sub(Temp, second):
        
        result = kasr()
        result.x = Temp.x*second.y - Temp.y*second.x
        result.y = Temp.y*second.y
        return result
    
    
    
    
    
    
    
    
    def Divide(Temp, second):
        
        result = kasr()
        result.x = Temp.x*second.y
        result.y = Temp.y*second.x
        return result
    



XX= list(map(int, input('Enter Number 1 (x/y)\n').split('/')))
YY= list(map(int, input('enter Number 2 (x/y)\n').split('/')))
a = kasr(XX[0], XX[1])
b = kasr(YY[0], YY[1])
print('sum: %s\t sub: %s\t mul: %s\t div: %s'%((a.Sum(b)).Show(), (a.Sub(b)).Show(), (a.Multiple(b)).Show(), (a.Divide(b)).Show()))