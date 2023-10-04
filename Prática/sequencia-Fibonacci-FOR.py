temp1 = 0
temp2 = 1
for i in range(1,11):
    print('(',i,'):',temp2)
    aux=temp2
    temp2 = temp1 + temp2
    temp1=aux