import pandas as pd
import datetime
from dateutil import parser


df_cons = pd.read_csv('./attendance.csv')
objects = df_cons.to_dict('records')
NAMES = []
for obj in objects:
    name = obj['Name']
    if name not in NAMES:
        NAMES.append(name)


for name in NAMES:
    with open('output.txt', 'a') as f:
        lines = lambda x: f.write(f'{x}\n')
        forName = f'\n\nFor: {name}.'
        lines(forName)
        print(forName)
        df = df_cons[(df_cons['Name']==name)].copy()
        df_time = df.copy()
        df_time['date'] = pd.to_datetime(df['Date/Time']).dt.date
        df_time = df_time.drop_duplicates(subset=['Status', 'date'], keep='first')

        In = df_time[(df_time['Status']=='C/In')].copy()
        Out = df_time[(df_time['Status']=='C/Out')].copy()
        InDict = In.to_dict('records')
        testDict = {}
        for dic in InDict:
            date = dic['Date/Time']
            outCheck = Out[(Out['date']==dic['date'])]['Date/Time']
            outCheck = outCheck.values
            if len(outCheck) >= 1:
                date = parser.parse(date)
                outCheck = parser.parse(outCheck[0])
                final = outCheck - date
                testDict[f'{date.date()}'] = [str(final).split(' ')[-1], [date, outCheck]]
        # print(testDict)
        total_hours = datetime.timedelta()
        for k, v in testDict.items():
            (h, m, s) = v[0].split(':')
            total_hours += datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            detail = f'Date: {k},  Working Hours={v[0]}, From: {v[1][0].time()} - {v[1][1].time()}.'
            lines(detail)
            print(detail)
        totsec = total_hours.total_seconds()
        h = int(totsec//3600)
        m = int((totsec%3600) // 60)
        sec =int((totsec%3600)%60)
        total_hours = f'{h}:{m}:{sec}'
        total = f'Total Days={len(testDict)}/22,  Total Hours={total_hours}/198:00:00'
        lines(total)
        print(total)
