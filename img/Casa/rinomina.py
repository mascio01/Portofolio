import os

# Usa la cartella corrente
cartella = os.getcwd()

# Nome della cartella (in minuscolo)
nome_cartella = os.path.basename(cartella).lower()

# Estensioni valide per immagini
estensioni_valide = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

# Filtra e ordina i file immagine
file_immagini = [f for f in os.listdir(cartella) if f.lower().endswith(estensioni_valide)]
file_immagini.sort()

# Rinomina le immagini in ordine sequenziale
for i, nome_vecchio in enumerate(file_immagini, start=1):
    estensione = os.path.splitext(nome_vecchio)[1].lower()
    nuovo_nome = f"{nome_cartella}{i}{estensione}"
    
    percorso_vecchio = os.path.join(cartella, nome_vecchio)
    percorso_nuovo = os.path.join(cartella, nuovo_nome)
    
    os.rename(percorso_vecchio, percorso_nuovo)
    print(f"{nome_vecchio} -> {nuovo_nome}")

print("Rinomina completata.")
