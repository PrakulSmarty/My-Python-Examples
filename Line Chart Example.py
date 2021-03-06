import pandas as pd
import matplotlib.pyplot as plt

target = pd.Series([5000,8000,10000,3000],index=["Zone1","Zone2","Zone3","Zone4"])
actual = pd.Series([6000,7000,11000,4000],index=["Zone1","Zone2","Zone3","Zone4"])
sales = {"TargetSales":target, "ActualSales":actual}
df = pd.DataFrame(sales)
df.plot()
plt.show()