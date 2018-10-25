str=''
for row in range(0,7):
        for col in range(0,7):
                if(col==1 or (row>2 and col==row-1) or (row<3 and col==5-row)):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)    
                    
