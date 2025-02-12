# %%
import pandas as pd
import numpy as np

# Creazione del dataframe con 10 righe e 4 colonne con valori casuali
data = np.random.randint(1, 100, size=(10, 4))  # Numeri casuali tra 1 e 100
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Stile per evidenziare le colonne con colori diversi
def highlight_columns(x):
    color = {
        'A': 'background-color: yellow',
        'B': 'background-color: lightgreen',
        'C': 'background-color: lightblue',
        'D': 'background-color: lightcoral'
    }
    return [color.get(col, '') for col in x.index]  # Restituire il colore per ogni colonna

# Applicare lo stile al dataframe
styled_df = df.style.apply(highlight_columns, axis=0)  # axis=0 per colonne

# Visualizzare direttamente il dataframe stilizzato
styled_df


# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Creazione del dataframe con 10 righe e 4 colonne con valori casuali
data = np.random.randint(1, 100, size=(10, 4))  # Numeri casuali tra 1 e 100
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Impostazioni della figura per la heatmap
plt.figure(figsize=(8, 6))

# Creare la heatmap
sns.heatmap(df, annot=True, cmap='YlGnBu', cbar=True, fmt='d', linewidths=0.5)

# Mostrare la heatmap
plt.show()


