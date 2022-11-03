import pandas as pd
import datetime

# df = pd.read_excel('./attendance_group.xls')
df_cons = pd.read_excel('./attendance_main.xls')
# df = read.groupby('Name')
# df = read.groupby('Date/Time')
# print(read.head())
# print(read.to_dict('records'))
# df = df.to_records('record')
# print(df)
objects = df_cons.to_dict('records')
NAMES = []
for obj in objects:
    name = obj['name']
    if name not in NAMES:
        NAMES.append(name)


for name in NAMES:
    with open('output.txt', 'a') as f:
        lines = lambda x: f.write(f'{x}\n')
        forName = f'\n\nFor: {name}.'
        lines(forName)
        print(forName)
        df = df_cons[(df_cons['name']==name)].copy()
        df_time = df.copy()
        df_time['date'] = pd.to_datetime(df['date/time']).dt.date
        df_time = df_time.drop_duplicates(subset=['status', 'date'], keep='first')

        In = df_time[(df_time['status']=='C/In')].copy()
        Out = df_time[(df_time['status']=='C/Out')].copy()
        InDict = In.to_dict('records')
        testDict = {}
        for dic in InDict:
            date = dic['date/time']
            outCheck = Out[(Out['date']==dic['date'])]['date/time']
            outCheck = outCheck.values
            if len(outCheck) >= 1:
                final = outCheck[0] - date
                testDict[f'{datetime.datetime.date(date)}'] = str(final).split(' ')[-1]
        # print(testDict)
        total_hours = datetime.timedelta()
        for k, v in testDict.items():
            (h, m, s) = v.split(':')
            total_hours += datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            detail = f'Date: {k},  Working Hours={v}'
            lines(detail)
            print(detail)
        totsec = total_hours.total_seconds()
        h = int(totsec//3600)
        m = int((totsec%3600) // 60)
        sec =int((totsec%3600)%60)
        total_hours = f'{h}:{m}:{sec}'
        total = f'Total Days={len(testDict)},  Total Hours={total_hours}'
        lines(total)
        print(total)









    # if pd.isnull(outCheck):
    #     print(outCheck)
    # else:
    #     print(outCheck)
# # In['start'] = pd.to_datetime(In['date/time'])
# # Out['end'] = pd.to_datetime(Out['date/time'])
# # df_time['diff'] = (In['start']-Out['end']).dt.total_seconds()
# df_time['diff'] = df_time.groupby('status').agg({'date/time': "diff"})
# # testing = pd.to_datetime(df_time['diff'])
# # test = df_time.groupby(['status', 'date'])['date/time'].sum()
# print(df_time)
# # grp = df.groupby(by=[df['date/time'].map(lambda x : (x.hour, x.minute))])

# # print(grp.count())
# # In['date/time'] = pd.to_datetime(In['date/time']).dt.date
# # In = In.drop_duplicates(subset='date/time', keep='first').to_dict('records')
# # Out = df[(df['status']=='C/Out')].copy()
# # Out['date/time'] = pd.to_datetime(Out['date/time']).dt.date
# # Out = Out.drop_duplicates(subset='date/time', keep='last')
# # final = []
# # for i in In:
# #     date = i['date/time']
# #     print(date)
# #     test = Out[(Out['date/time'] == date)].to_dict('records')
# #     final.append(test)
# #     print('Done')
# # # Out['date/time'] = pd.to_datetime(In['date/time']).dt.date
# # # Out = Out.drop_duplicates(subset='date/time', keep='last')
# # print(final)
