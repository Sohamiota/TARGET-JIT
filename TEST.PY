import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

data = [10, 12, 15, 18, 22, 25, 30]
df = pd.Series(data)

model = ARIMA(df, order=(1,1,1))
result = model.fit()

print(result.summary())
