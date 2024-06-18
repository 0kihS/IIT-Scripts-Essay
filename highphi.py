import numpy as np
import pyphi

n = 6  # Hoeveelheid poorten of "Nodes" 
# Hoe meer nodes, hoe groter de complexiteit van de berekening, en hoe groter Φ vanwege de gestructureerde aard van het netwerk

# Genereer een TPM op basis van een NumPy array
def genereer_gestructureerde_tpm(n):
    tpm = np.zeros((2**n, n))
    
    # Vul de array volgens een gedetermineerde regel
    for i in range(2**n):
        binaire_staat = np.array(list(np.binary_repr(i, width=n)), dtype=int)
        
        # Elke Node node hangt af van de XOR van de staat van de nodes (i+1) % n en (i+2) % n
        for j in range(n):
            staat_kolom = binaire_staat[(j + 1) % n] ^ binaire_staat[(j + 2) % n]
            tpm[i, j] = staat_kolom
    
    return tpm

# Dit is het volledige ontwerp van ons netwerk, vanaf hier berekenen we de Φ

# Genereer de TPM met hoeveelheid nodes n
tpm = genereer_gestructureerde_tpm(n)
log(tpm)

network = pyphi.Network(tpm)

# Definieer een initiele staat van de tpm (in dit geval met alleen nullen om complexiteit te besparen)
state = tuple([0] * n)

# Definieer een "subsysteem" van het netwerk om de Φ van te berekenen.
subsystem = pyphi.Subsystem(network, state)

# Bereken Φ
phi = pyphi.compute.phi(subsystem)

print(f"Φ voor dit netwerk: {phi}")
