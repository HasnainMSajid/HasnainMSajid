#This script will work in hamilton
# In hamilton need to activate virtual environment
#for the first time install pandas using command; pip install pandas
import pandas as pd
#for editing in excell sheet need to install library; pip install aspose-cells

df = pd.read_csv('energy_data.out', sep='\t')

df=df.to_excel('energy_data.xlsx', 'Sheet1', index=False)

