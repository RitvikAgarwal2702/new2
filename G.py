str=''
for row in range(0,7):
        for col in range(0,7):
                if(
                    (col==1 and row not in (0,6)) or (row in (0,6) and col not in (0,1,6)) or (col==6 and row in (1,4,5)) or (row==4 and col>2)):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)    
                    
