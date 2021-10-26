# Imports
import pandas as pd
import numpy as np
from datetime import datetime

## Access Data From Google Console Bucket
fraud_data_original = pd.read_json("fraud_dataset/data.json").set_index("object_id")

fraud_data_original.info()
fraud_data_original.describe()
fraud_data_original.head()

# Creating Columns
fraud_data_original['Fraud'] = fraud_data_original.apply(lambda x: 1 if ('fraud' in x['acct_type']) else 0, axis = 1) 
fraud_data_original['Classified'] = 'Not Classified'

# Plots
mop = sns.countplot(x = 'Fraud', data = fraud_data_original)
for label in mop.patches:
  mop.annotate(f'\n{label.get_height()}',
              (label.get_x() + 0.40, label.get_height()),
              ha ='center', 
              va ='top', 
              color = 'white',
              size = 10)
mop.set_title("Fraud Dataset Distribution Balance")
mop.set_ylabel("Number of Records Classified")





## --- End --- ##
## Save Perfect Dataset to file
