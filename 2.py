#Series
import pandas as pd
a=[1,3,5,7,9]
y=pd.Series(a)
print(y)

import pandas as pd
a=["Nsk",3,5]
y=pd.Series(a,index=[1,"y","z"])
print(y)


