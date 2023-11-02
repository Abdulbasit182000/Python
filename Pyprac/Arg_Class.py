import argparse
import pandas as pd
import datetime

def cehckdate(df,start,end):
    y = pd.to_datetime(end)
    x = pd.to_datetime(start) 
    df1 = df.sort_values(by=['Date.Full'])
    first_date = df1['Date.Full'].iloc[0]
    if first_date >= x and x <= y:
        return True
    else:
        return False


class Par:
    def __init__(self):
        self.parser=argparse.ArgumentParser(description="Base parsers")
        self.parser.add_argument('--file',type=str,help="File name")
        self.parser.add_argument('--range',type=str,help="Date in range 2023-01-01 to 2023-01-31")
        self.parser.add_argument('--max',action='store_true',help='Max of column')
        self.parser.add_argument('--min',action='store_true',help='Min of column')
        self.parser.add_argument('--mean',action='store_true',help='Mean of column')
        self.parser.add_argument('--column',type=str,help="Column name")
        self.parser.add_argument('--export',type=str,help='Export data to filename')
        self.parser.add_argument('--pr',type=str,help="What collums should be printed x,y,x,etc")
    
class newpar(Par):
    def __init__(self):
        super().__init__()
    
    def maxvalue(self,df,column):
        if column in df.columns:
            maxval=df[column].max()
            print(maxval)
    def minvalue(self,df,column):
        if column in df.columns:
            minval=df[column].min()
            print(minval)
    def maxval1(self,df,column,y,a):
        maxval=df[column].max()
        df2 = df[df[column] == maxval]
        if a:
            df3=df2[y]
            df3.to_csv(a,index=False)
        else:
            print(df2[y])
    def minval1(self,df,column,y,a):
        minval=df[column].min()
        df2 = df[df[column] == minval]
        if a:
            df3=df2[y]
            df3.to_csv(a,index=False)
        else:
            print(df2[y])
    def meanvalue(self, df, y,a):
        # Calculate the descriptive statistics for the entire DataFrame
        df1 = df.describe()
        df2 = df1[y]
        # Drop unnecessary descriptors (count, min, std, 25%, 50%, 75%, max)
        descriptors_to_drop = ['count', 'min', 'std', '25%', '50%', '75%', 'max']
        df3 = df2.drop(descriptors_to_drop)
        if a:
            df3.to_csv(a,index=False)
        else:
            print(df3)
if __name__=='__main__':
    parser=newpar()
    args=parser.parser.parse_args()
    global x
    global df
    global li
    global dr
    global dr1
    global dr2
    global w
    li=[]
    if args.file:
        x=str(args.file)
        if(x.endswith('.csv')):
            df=pd.read_csv(args.file,sep=',')
        else:
            args.file=False
            print('Please Enter csv file')
    if args.export:
        w=str(args.export)
        if(w.endswith('.csv')):
            pass
        else:
            args.export=False
            print('Please Enter all files in .csv format')
    if args.range:
         dr=str(args.range).split(" to ")
         global start, end
         start=dr[0]
         end=dr[1]
         if(args.file):
             df['Date.Full']=pd.to_datetime(df['Date.Full'])
             if(cehckdate(df,start,end) is False):
                 print('error in dates')
         else:
            print('enter file first')
    else:
        args.range=False
        print('range not present')
    if args.column and args.file:
        x=args.column
        if(x in df.columns):
            pass
        else:
            print('not in df')
            args.column=False
    else:
        args.column=False
    if args.pr:
        if ',' in args.pr:
            dr1=str(args.pr).split(',')
            for i in dr1:
                if i in df.columns:
                    li.append(i)
                else:
                    args.pr=False
                    print('not in df list')
        else:
            dr2=args.pr
            if dr2 in df.columns:
                pass
            else:
                print('not in df')
                args.pr=False
    if args.max:
        if(not args.column):
            print('no column provided')
        elif(not args.file):
            print('Issue with file')
        elif(args.range):#for if range is specified
            if(args.pr):
                if(args.export):
                    df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                    if len(li)==0:
                        parser.maxval1(df1,x,dr2,w)
                    else:
                        parser.maxval1(df1,x,li,w)
                else:
                    df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                    if len(li)==0:
                        parser.maxval1(df1,x,dr2,False)
                    else:
                        parser.maxval1(df1,x,li,False)

            else:
                df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                parser.maxvalue(df1,x)
        else:
            if(args.pr):
                if(args.export):
                    if len(li)==0:
                        parser.maxval1(df,x,dr2,w)
                    else:
                        parser.maxval1(df,x,li,w)
                else:
                    if len(li)==0:
                        parser.maxval1(df,x,dr2,False)
                    else:
                        parser.maxval1(df,x,li,False)
            else:
                parser.maxvalue(df,x)
    if args.min:
        if(not args.column):
            print('no column provided')
        elif(not args.file):
            print('Issue with file')
        elif(args.range):#for if range is specified
            if(args.pr):
                if(args.export):
                    df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                    if len(li)==0:
                        parser.minval1(df1,x,dr2,w)
                    else:
                        parser.minval1(df1,x,li,w)
                else:
                    df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                    if len(li)==0:
                        parser.minval1(df1,x,dr2,False)
                    else:
                        parser.minval1(df1,x,li,False)

            else:
                df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                parser.minvalue(df1,x)
        else:
            if(args.pr):
                if(args.export):
                    if len(li)==0:
                        parser.minval1(df,x,dr2,w)
                    else:
                        parser.minval1(df,x,li,w)
                else:
                    if len(li)==0:
                        parser.minval1(df,x,dr2,False)
                    else:
                        parser.minval1(df,x,li,False)
            else:
                parser.maxvalue(df,x)
    if args.mean:
        if(args.column):
            print('column not required,use --pr instead to print values of all columns')
        elif(not args.file):
            print('Issue with file')
        elif(args.range):#for if range is specified
            if(args.pr):
                if(args.export):
                    df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                    if len(li)==0:
                        parser.meanvalue(df1,dr2,w)
                    else:
                        parser.meanvalue(df1,li,w)
                else:
                    df1=df[(df['Date.Full']>=start) & (df['Date.Full']<=end)]
                    if len(li)==0:
                        parser.meanvalue(df1,dr2,False)
                    else:
                        parser.meanvalue(df1,li,False)
        else:
            if(args.pr):
                if(args.export):
                    if len(li)==0:
                        parser.meanvalue(df,dr2,w)
                else:
                     parser.meanvalue(df,li,False)