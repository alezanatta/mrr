import numpy as np
import pandas as pd

df = pd.read_csv("pagamentos.csv", sep=",", header=None)
df.columns = ["cd_cliente", "dt_pagamento", "vl_pagamento", "plano"]





print(df.head())