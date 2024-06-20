import numpy as np
import pyphi

n = 5  # Hoeveelheid poorten of "Nodes" 

# Genereer een TPM 
def genereer_willekeurige_tpm(n):
    # Creer een tpm met de vorm (2^n, n), gevuld met compleet willekeurige getallen
    tpm = np.random.rand(2**n, n)
    
    # Normaliseer de tpm zodat elke rij op 1 uitkomt onder de streep. (PyPhi forceert stochastische matrices)
    tpm = tpm / tpm.sum(axis=1, keepdims=True)
    
    return tpm

# Dit is het volledige ontwerp van ons netwerk, vanaf hier berekenen we de Φ

# Genereer de TPM met hoeveelheid nodes n
tpm = genereer_willekeurige_tpm(n)
print(tpm)

network = pyphi.Network(tpm)

# Definieer een initiele staat van de tpm (in dit geval met alleen nullen om complexiteit te besparen)
state = tuple([0] * n)

# Definieer een "subsysteem" van het netwerk om de Φ van te berekenen.
subsystem = pyphi.Subsystem(network, state)

# Bereken Φ
phi = pyphi.compute.phi(subsystem)

print(f"Φ voor dit netwerk: {phi}")
