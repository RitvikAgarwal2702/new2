str=''
for row in range(0,7):
        for col in range(0,7):
                if(col==1 or (row==6 and col!=0)):
                        str=str+'*'	    
                else:
                        str=str+' '
        str=str+'\n'
print(str)    
                    
