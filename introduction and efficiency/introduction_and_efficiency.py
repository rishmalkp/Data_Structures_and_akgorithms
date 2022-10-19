class Classy(object):
    
    items=[]
    def addItem(self, item):
        self.items.append(item)
        return self.items
        
    
    def getClassiness(self):
        upitems=self.items
        rate=0
        for i in upitems:
            if(i=='tophat'):
                rate=rate+2
            elif(i=='bowtie'):
                rate=rate+4
            elif(i=='monocle'):
                rate=rate+5
            else:
                pass
        return rate
                
        

me = Classy()
me.getClassiness()
me.addItem("tophat")
print(me.getClassiness())
me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
print(me.getClassiness())
me.addItem("bowtie")
print(me.getClassiness())