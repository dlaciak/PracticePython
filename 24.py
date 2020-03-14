def KreskiPoziome(RozmiarPlanszy):
    for i in range(RozmiarPlanszy):
        if i == 0:
            print(' ---',end='')
        if i > 0 and i < RozmiarPlanszy - 1:
            print(' ---',end='')
        if i == RozmiarPlanszy - 1:
            print(' --- ',)
            
def KreskiPionowe(RozmiarPlanszy):
    for i in range(RozmiarPlanszy):
        if i == 0:
            print('|   ',end='')
        if i > 0 and i < RozmiarPlanszy - 1:
            print('|   ',end='')
        if i == RozmiarPlanszy - 1:
            print('|   |',)



if __name__ == "__main__":

    RozmiarPlanszy = int(input())
    for i in range(RozmiarPlanszy):
        KreskiPoziome(RozmiarPlanszy)
        KreskiPionowe(RozmiarPlanszy)
        KreskiPoziome(RozmiarPlanszy)





        




