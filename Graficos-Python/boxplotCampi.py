import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import glob
import os


plt.rcParams.update({
    "font.family": "serif",     
    "font.size": 10,
    "axes.linewidth": 1.0,
    "xtick.direction": "in",     
    "ytick.direction": "in",
    "grid.linestyle": "--",      
    "grid.alpha": 0.4
})


arquivos_txt = glob.glob("*.txt")
lista_dataframes = []
for arquivo in arquivos_txt:
    nome = os.path.basename(arquivo).replace('.txt', '')
    try:
        df_temp = pd.read_csv(arquivo, sep=r'\s+')
    except:
        df_temp = pd.read_csv(arquivo, sep=r'\t')
    df_temp['Origem'] = nome
    lista_dataframes.append(df_temp)

df_final = pd.concat(lista_dataframes, ignore_index=True)


paleta_artigo = ["#7b1fa2", "#2e7d32", "#0277bd", "#8d6e63", "#f9a825"]

fig, ax = plt.subplots(figsize=(10, 6))


sns.boxplot(
    x='Origem', y='media_individual', data=df_final, 
    hue='Origem', palette=paleta_artigo, legend=False, showfliers=False, ax=ax
)


n_boxes = len(df_final['Origem'].unique())

lines_per_box = len(ax.lines) // n_boxes

for i, patch in enumerate(ax.patches):
    col = paleta_artigo[i % len(paleta_artigo)]
    rgb_color = mcolors.to_rgb(col)
    

    patch.set_facecolor((*rgb_color, 0.2))
    patch.set_edgecolor(col)
    patch.set_linewidth(1.5)


    for j in range(i * lines_per_box, (i + 1) * lines_per_box):
        ax.lines[j].set_color(col)
        ax.lines[j].set_linewidth(1.5)


sns.stripplot(
    x='Origem', y='media_individual', data=df_final, 
    color='black',       
    alpha=0.3,           
    jitter=True, 
    size=4, 
    ax=ax
)


plt.xlabel('Campus / Unidade Acadêmica', weight='bold')
plt.ylabel('Média Individual', weight='bold')
plt.grid(axis='y')


sns.despine(top=False, right=False)

plt.tight_layout()

# plt.savefig('boxplot_campi.png', dpi=300)
plt.show()