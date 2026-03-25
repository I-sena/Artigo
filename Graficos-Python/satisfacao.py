import matplotlib.pyplot as plt
import pandas as pd


plt.rcParams.update({
    "font.family": "serif",      
    "font.size": 10,             
    "axes.linewidth": 1.0,       
    "xtick.direction": "in",     
    "ytick.direction": "in",
    "figure.facecolor": "white"
})


dados = {
    'Eixo': [
        'Eixo 1: Planejamento e Avaliação Institucional',
        'Eixo 2: Desenvolvimento Institucional',
        'Eixo 3: Políticas Acadêmicas',
        'Eixo 4: Políticas de Gestão',
        'Eixo 5: Infraestrutura e Condições de Trabalho'
    ],
    'Aprovação (%)': [76.72, 73.04, 65.17, 57.91, 54.80]
}

df = pd.DataFrame(dados)


cores = ["#28a745", "#dc3545"] 

for index, row in df.iterrows():
    labels = ['Satisfação', ''] 
    valores = [row['Aprovação (%)'], 100 - row['Aprovação (%)']]
    
    fig, ax = plt.subplots(figsize=(4, 4))
    
    
    wedges, texts, autotexts = ax.pie(
        valores,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=cores,
        pctdistance=0.75, 
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.8} 
    )

   
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')


    ax.axis('equal') 

    nome_arquivo = f"grafico_eixo_{index+1}.png"

    # plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    plt.show() 