#UUDD

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


#enter gene and site 
gene = 'ABCC1'
site = 'S918'

# Load data from the Excel file
filepath=r"C:\Users\Admin\Downloads\ABCC1_S918__UUDD_final_Data1_Bin_comp_Filtered_Top25_Extracted (1).xlsx"
sheet_name="Sheet1"

df = pd.read_excel(filepath,sheet_name=sheet_name)


formatted_data = []
x_spacing = max(30, len(df) // 10)  
xaxis = x_spacing

for _, row in df.iterrows():
    formatted_data.append(
        {"xaxis": xaxis, "yaxis": row["SUM_UU"], "side": "bottom", "color": "#429C22", "site2": row["site2"]}
    )
    formatted_data.append(
        {"xaxis": xaxis, "yaxis": row["SUM_DD"], "side": "top", "color": "#CF0000", "site2": row["site2"]}
    )
    xaxis += x_spacing

plot_data = pd.DataFrame(formatted_data)

fig_width = max(6, len(df) / 10)  
plt.figure(figsize=(fig_width, 5))

ax = plt.gca()
ax.set_facecolor("#FFF")

top_data = plot_data[plot_data["side"] == "top"]
bottom_data = plot_data[plot_data["side"] == "bottom"]

plt.vlines(
    top_data["xaxis"], 0, top_data["yaxis"], color=top_data["color"], label="Top", lw=1.8
)
plt.vlines(
    bottom_data["xaxis"], 0, -bottom_data["yaxis"], color=bottom_data["color"], label="Bottom", lw=1.8
)

plt.yticks(np.arange(-15, 21, 5))
plt.ylabel("Frequency of the top negatively correlated protein phosphosites", fontsize=8)
ax.set_xticks([])

# Add a legend with descriptive labels
legend_patches = [
       Patch(facecolor='#CF0000', label='Upregulated PSOPs in MAST2 S1504 Downregulated datasets (DU)', edgecolor='black'),
    Patch(facecolor='#429C22', label='Downregulated PSOPs in MAST2 S1504 Upregulated datasets (UD)', edgecolor='black')
]
plt.legend(
    handles=legend_patches,
    bbox_to_anchor=(0.90, 0.98),
    fancybox=True,
    framealpha=1.0,
    bbox_transform=plt.gcf().transFigure,
    loc="upper right",
    fontsize=8,
)


fixed_y = 10 # Fixed y-position for annotations

for _, row in top_data.iterrows():  
    plt.annotate(row['site2'], xy=(row['xaxis'], fixed_y),  xytext=(row['xaxis'], fixed_y+1.2), ha='center', va='bottom', rotation=90, fontsize=6)



ax.axhline(y=0, color="gray", linestyle="-", lw=0.5)

plt.savefig(f"{gene}_{site}_UUDD_plot.svg", format="svg", dpi=300)


