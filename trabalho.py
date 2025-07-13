from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
import pandas as pd

dados = {
    "Sul": {
        "data": ["2025-07-11", "2025-07-12", "2025-07-13"],
        "temperatura": [13, 15, 12] 
    },
    "Norte": {
        "data": ["2025-07-11", "2025-07-12", "2025-07-13"],
        "temperatura": [31, 32, 30] 
    }
}


def pegar_dados(regiao):
    df = pd.DataFrame(dados[regiao])       
    df["data"] = pd.to_datetime(df["data"]) 
    return df


regiao_atual = "Sul"
df_inicial = pegar_dados(regiao_atual)
fonte = ColumnDataSource(df_inicial)  


grafico = figure(title="Temperatura por Dia", x_axis_type="datetime", width=700, height=400)
grafico.line(x="data", y="temperatura", source=fonte, line_width=2, color="green")
grafico.xaxis.axis_label = "Data"
grafico.yaxis.axis_label = "Temperatura (°C)"


menu = Select(title="Região:", value="Sul", options=["Sul", "Norte"])


def atualizar(attr, old, new):
    nova_regiao = menu.value
    novo_df = pegar_dados(nova_regiao)
    fonte.data = ColumnDataSource.from_df(novo_df)

menu.on_change("value", atualizar)


layout = column(menu, grafico)
curdoc().add_root(layout)

# Executa com bokeh serve --show trabalho.py :)
