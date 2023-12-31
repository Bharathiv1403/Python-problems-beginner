#Dictionary use College Attenent Sheet
import pandas as pd
Data= {
    "Student":["NAME","Bharathi","Bharath","Lokeswaran","Prem","Ranjith","Sridar","Vijay"],
    "Comeing_days":["DAYS",125,132,128,116,101,92,117]
    }
# y=pd.Series(Comeing_days,Student)
y=pd.DataFrame(Data)
print(y)