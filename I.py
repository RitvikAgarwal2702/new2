str=''
for row in range(0,7):
        for col in range(0,7):
                if(col==3 or (row in (6,0) and col not in(0,6))):
                        str=str+'*'	    
                else:
                        str=str+' '
        str=str+'\n'
print(str)    
                    
