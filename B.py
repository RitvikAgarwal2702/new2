str=''
for row in range(0,7):
        for col in range(0,7):
                if((col==1 and row not in (0,6)) or (row in (0,6) and (col>1 and col<6)) or (col==6 and row in (1,5))):
                        str=str+'* '	    
                else:
                        str=str+'  '
        str=str+'\n'
print(str)
print("hey")
                    
