import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({
    "font.family": "serif",     
    "font.size": 10,
    "axes.linewidth": 1.2,        
    "figure.facecolor": "white",
    "grid.linestyle": "--",      
    "grid.alpha": 0.7
})


dados_brutos = {
    'Eixo 1: Planejamento': ([1] * 23) + ([2] *44) + ([3] * 102) + ([4] *177) + ([5] * 211) + ([6] * 169), 
    'Eixo 2: Desenvolvimento': ([1] * 184) + ([2] *257) + ([3] * 521) + ([4] *760) + ([5] * 917) + ([6] * 929), 
    'Eixo 3: Políticas Acadêmicas': ([1] * 854) + ([2] * 905) + ([3] * 1489) + ([4] * 2019) + ([5] * 2071) + ([6] * 1987), 
    'Eixo 4: Políticas de Gestão': ([1] * 770) + ([2] * 601) + ([3] * 806) + ([4] * 1073) + ([5] * 1027) + ([6] * 895), 
    'Eixo 5: Infraestrutura': ([1] * 1630) + ([2] * 995) + ([3] * 1424) + ([4] * 1625) + ([5] * 1560) + ([6] * 1724) 
}


niveis = [1, 2, 3, 4, 5, 6]
dados_contados = {nome: pd.Series(notas).value_counts().reindex(niveis, fill_value=0).sort_index() 
                  for nome, notas in dados_brutos.items()}

df = pd.DataFrame(dados_contados)
df_percentual = (df.div(df.sum(axis=0), axis=1) * 100).round(1)


categorias_plot = ['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5', 'Nota 6']
num_vars = len(categorias_plot)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1] 

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

cores_artigo = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
nomes_eixos = df_percentual.columns.tolist()

for i, (nome_eixo, cor) in enumerate(zip(nomes_eixos, cores_artigo)):
    values = df_percentual[nome_eixo].values.flatten().tolist()
    values += values[:1]
    
    
    ax.plot(angles, values, color=cor, linewidth=2, label=nome_eixo)
    ax.fill(angles, values, color=cor, alpha=0.15)


ax.set_xticks(angles[:-1])
ax.set_xticklabels(categorias_plot, size=10, weight='bold')


ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)

plt.yticks([5, 10, 15, 20,25,30], ["5%","10%","15%", "20%","25%", "30%"], color="grey", size=8)

plt.ylim(0, 30)


plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), 
           ncol=2, frameon=True, edgecolor='black', fontsize=9)


plt.tight_layout()

# plt.savefig("radar_eixos.png", dpi=300, bbox_inches='tight')
plt.show()