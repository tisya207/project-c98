def swipefileData():
    swapFileName=input('enter the file name you want to swap ')
    swapedFileName=input('enter the file name you want your file to be swaped with ') 
    with open(swapFileName,'r') as file1:
        data_a= file1.read()

    with open(swapedFileName,'r') as file2:
        data_b= file2.read()


    with open(swapFileName,'w') as file1:
        file1.write(data_b)

    with open(swapedFileName,'w') as file2:
        file2.write(data_a)

swipefileData()