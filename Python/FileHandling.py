import os
## Open in read mode
#infile=open('myfile.txt','r')

## Reads the entire file
## print(infile.read())

#print('')
#print('')

## Readline
#infile2=open('myfile.txt','r')
#line=infile2.readlines()
#print(line)
##infile.close()

##
#lines=open('myfile.txt').read()
#print(lines)

##
#lines=open('myfile.txt').read().splitlines()
#print(lines)

#with open('myfile.txt','r')as infile:
    #for line in infile:
        #print(line,end='')


#infile=open('myfile.txt','r').read()
#print(infile)

## Writing to file
## this is opening it in just the write file so we only see what we wrote not the whole file.
##output=open('myfile.txt','w')
#output.write("7\n")
#output.close()

## Append to a file
## add new lines to a file
#output2=open('myfile.txt','a')
#output2.write("boo\n")
#output2.close()

## write list items to different lines
## \n means new line
#fruits=['oranges\n','mangoes\n']
#output2.writelines(fruits)
#output2.close()

##for fruit in fruits:
##  output2.write(fruit)
##   output.write("\n")

#output2.write("pineapple,banana")
#output2.close()

os.remove('myfile.txt')








