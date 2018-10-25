str=''
for row in range(0,7):
        for col in range(0,7):
                if(col==1 or (row in (0,6) and (col>0 and col<5)) or (col==6 and row in (2,3,4)) or (col==5 and row in (1,5))):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)    
                    
