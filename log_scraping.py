import re
import pandas as pd
r = re.compile('././.{4} .{2}:.{2}')
with open('/Users/arjunkavungal/Downloads/web_activity.log','r') as f:
    lines = [line.rstrip() for line in f]
data = []
full = pd.DataFrame()
ip = '0.0.0'
for i in lines:
    if i.count('.') == 3:
        ip = i
        print('previous ip' + ip)
        print('previous data')
        df = pd.DataFrame(data[1:], columns=[0])
        df = df.iloc[:,0].str.split('\"', expand=True)
        df = df.replace({'}':''}, regex=True)
        df = df.replace({'{':''}, regex=True)
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        for j in range(len(df)):
            if type(df.iloc[j,2]) == type('A') and "(" not in df.iloc[j,2]:
                df.iloc[j,2] = df.iloc[j,4]
                df.iloc[j,4] = ""
        df['ip'] = ip
        full = pd.concat([full,df])

    else:
        data.append(i)
print(full)
