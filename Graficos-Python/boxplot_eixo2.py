import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.linewidth": 1.0,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "grid.linestyle": "--",
    "grid.alpha": 0.4
})


respostas_p1 = ([1] * 29) + ([2] *47) + ([3] * 84) + ([4] *118) + ([5] * 146) + ([6] * 132) 
respostas_p2 = ([1] * 24) + ([2] *30) + ([3] * 67) + ([4] *100) + ([5] * 161) + ([6] * 194)
respostas_p3 = ([1] * 40) + ([2] *32) + ([3] * 73) + ([4] *112) + ([5] * 140) + ([6] * 182)
respostas_p4 = ([1] * 22) + ([2] *22) + ([3] * 87) + ([4] *137) + ([5] * 192) + ([6] * 159)
respostas_p5 = ([1] * 39) + ([2] *60) + ([3] * 101) + ([4] *143) + ([5] * 137) + ([6] * 139)
respostas_p6 = ([1] * 30) + ([2] *66) + ([3] * 109) + ([4] *150) + ([5] * 141) + ([6] * 123)

dados = {
    'Pergunta 1': respostas_p1,
    'Pergunta 2': respostas_p2,
    'Pergunta 3': respostas_p3,
    'Pergunta 4': respostas_p4,
    'Pergunta 5': respostas_p5,
    'Pergunta 6': respostas_p6
}

dados_longos = []
for pergunta, respostas in dados.items():
    for resposta in respostas:
        dados_longos.append({'Pergunta': pergunta, 'Resposta': resposta})

df_respostas_longo = pd.DataFrame(dados_longos)


paleta_artigo = ["#7b1fa2", "#2e7d32", "#0277bd", "#8d6e63", "#f9a825"]

fig, ax = plt.subplots(figsize=(12, 7))


sns.boxplot(
    x='Pergunta', y='Resposta', data=df_respostas_longo, 
    hue='Pergunta', palette=paleta_artigo, legend=False, ax=ax
)


n_boxes = len(df_respostas_longo['Pergunta'].unique())
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


plt.xlabel('Perguntas', weight='bold')
plt.ylabel('Valores das Respostas', weight='bold')
plt.grid(axis='y')


sns.despine(top=False, right=False)

plt.tight_layout()

# plt.savefig('boxplot_eixo2.png', dpi=300)
plt.show()