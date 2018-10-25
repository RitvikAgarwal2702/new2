str=''
for row in range(0,7):
        for col in range(0,8):
                if(col in (1,7) or (row>2 and (col==row+1 or col==7-row))):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)    
                    
