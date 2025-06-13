import geopandas as gpd 
import matplotlib.pyplot as plt 
 
# Load world map 
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')) 
 
# Filter for Asian countries 
asia = world[world['continent'] == 'Asia'] 
 
# Create plot 
fig, axs = plt.subplots(1, 2, figsize=(14, 6)) 
 
# Plot code as text on the left 
code_text = """ 
import geopandas as gpd 
import matplotlib.pyplot as plt 
 
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')) 
asia = world[world['continent'] == 'Asia'] 
 
fig, axs = plt.subplots(1, 2, figsize=(14, 6)) 
 
asia.plot(ax=axs[1], color='lightgray', edgecolor='black') 
asia[asia.name == 'Iran'].plot(ax=axs[1], color='green') 
 
axs[1].set_title('Map of Asia with Iran Highlighted') 
axs[1].axis('off') 
 
plt.show() 
""" 
 
axs[0].text(0, 1, code_text, fontsize=10, fontfamily='monospace', va='top', wrap=True) 
axs[0].axis('off') 
axs[0].set_title('Python Code') 
 
# Plot Asia map on the right 
asia.plot(ax=axs[1], color='lightgray', edgecolor='black') 
asia[asia.name == 'Iran'].plot(ax=axs[1], color='green') 
 
axs[1].set_title('Map of Asia with Iran Highlighted') 
axs[1].axis('off') 
 
plt.tight_layout() 
plt.savefig('/mnt/data/asia_iran_map_code_sidebyside.png') 
plt.show()
