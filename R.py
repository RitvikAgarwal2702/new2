str=''
for row in range(0,8):
        for col in range(0,8):
                if((col==1 and row!=0) or ((row==0 or row==3)and(col>1 and col<5)) or (row in (1,2,7) and col==5) or (row>3 and row==col+2)):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)    
                    
