import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv(r"C:\Users\OMEN\Downloads\ganga_water_level.csv")
df = df.sort_values('annual_max_water_level_m', ascending=False).reset_index(drop=True)

n = len(df)
df['rank'] = df.index + 1
df['T'] = (n + 1) / df['rank']  
df['AEP'] = 1 / df['T']         

gumbel_params = stats.gumbel_r.fit(df['annual_max_water_level_m'], floc=0)
df['gumbel_fit'] = stats.gumbel_r.ppf(1 - 1/df['T'], *gumbel_params)

plt.figure(figsize=(8,5))
plt.scatter(df['T'], df['annual_max_water_level_m'], color='blue', label='Observed annual maxima')
plt.plot(df['T'], df['gumbel_fit'], 'r--', label='Gumbel distribution fit')
plt.xscale('log')
plt.xlabel('Recurrence Interval (years) – log scale')
plt.ylabel('Annual Maximum Water Level (m)')
plt.title('Flood Frequency Analysis – Ganga River (DAHITI station 19519)')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('recurrence_plot.png', dpi=300)
plt.show()

print("Return Period (years) | Estimated Water Level (m)")
print("-----------------------------------------------")
for t in [2, 5, 10, 25, 50, 100]:
    level = stats.gumbel_r.ppf(1 - 1/t, *gumbel_params)
    print(f"{t:>20} | {level:>10.2f}")