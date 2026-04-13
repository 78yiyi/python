subjects=["MME","AO","RL","SOM","IPEI","FP"]
try:
    print(subjects[10])
except IndexError:
    print(f"Posición de lista no valida")