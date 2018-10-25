str=''
for row in range(0,7):
        for col in range(0,14):
                if(col==row+1 or col==13-row):
                        str=str+'*'	    
                else:
                        str=str+' '
        str=str+'\n'
print(str)    
                    
