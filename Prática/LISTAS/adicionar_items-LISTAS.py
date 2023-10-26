#append adiciona um valor a sua lista, mas apenas no final
#insert faz a mesma função do append, mas a grande diferença é que o insert pode adicionar um valor em qualquer lugar da lista

lanche = ['Hambúrguer','Suco','Pizza','Pudim']
lanche.append('Cookies') #resultado será -> ['Hambúguer','Suco','Pizza','Pudim','Cookies'] // Não se pode passar mais de um parâmetro para o append

lanche.insert(0,'Hot-Dog') #resultado será -> ['Hot-Dog','Hambúguer','Suco','Pizza','Pudim','Cookies']