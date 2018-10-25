str=''
for row in range(0,7):
        for col in range(0,7):
                if((col in (1,5) and row!=0) or (row in (0,3) and (col>1 and col<5))):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)    
                    
