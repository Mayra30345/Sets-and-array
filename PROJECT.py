def sym_difference(set1,set2):
    print("\n original set:   ")
    print(set1)
    print(set2)
    print("\n Symmetric difference of setc1 -setc2:   ")
    result=set1.symmetric_difference(set2)
    return result
seta1=set(['Green','Blue'])
seta2=set(["Blue","Yellow"])

print("Results of A sets")
sym_difference(seta1,seta2)


    