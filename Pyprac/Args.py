import argparse
import pandas as pd
import datetime


def cehckdate(df, start, end):
    y = pd.to_datetime(end)
    x = pd.to_datetime(start)
    df1 = df.sort_values(by=["Date.Full"])
    first_date = df1["Date.Full"].iloc[0]
    if first_date >= x and x <= y:
        return True
    else:
        return False


class Par:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Base parsers")
        self.parser.add_argument("--file", type=str, help="File name")
        self.parser.add_argument(
            "--range", type=str, help="Date in range 2023-01-01 to 2023-01-31"
        )
        self.parser.add_argument("--max", action="store_true", help="Max of column")
        self.parser.add_argument("--min", action="store_true", help="Min of column")
        self.parser.add_argument("--mean", action="store_true", help="Mean of column")
        self.parser.add_argument("--column", type=str, help="Column name")
        self.parser.add_argument("--export", type=str, help="Export data to filename")
        self.parser.add_argument(
            "--pr", type=str, help="What collums should be printed x,y,x,etc"
        )

    def file_validation(self, file):
        if file:
            x = str(file)
            if x.endswith(".csv"):
                df = pd.read_csv(file, sep=",")
                return df
            else:
                raise Exception("Please enter csv file")
        else:
            raise Exception("File not entered.")

    def export_validation(self, file):
        if file:
            x = str(file)
            if x.endswith(".csv"):
                return x
            else:
                raise Exception("Please enter csv file")

    def range_validation(self, range, df):
        if range:
            dr = str(range).split(" to ")
            start = dr[0]
            end = dr[1]
            df["Date.Full"] = pd.to_datetime(df["Date.Full"])
            if cehckdate(df, start, end) is False:
                raise Exception("Dates do not align")
            else:
                df1 = df[(df["Date.Full"] >= start) & (df["Date.Full"] <= end)]
                return df1
        else:
            return False

    def column_validation(self, column, df):
        if column:
            if column in df.columns:
                return column
            else:
                raise Exception("Column name not in DataFrame")
        else:
            return False

    def print_validation(self, pr, df):
        li = []
        if pr:
            if "," in pr:
                dr1 = str(pr).split(",")
                for i in dr1:
                    if i in df.columns:
                        li.append(i)
                    else:
                        raise Exception("The printing collums are not in file")
            else:
                dr2 = pr
                if dr2 in df.columns:
                    li.append(dr2)
                else:
                    raise Exception("The printing collums are not in file")
            return li
        else:
            return False

    def max_value(self, df, column, prin, export):
        x = [
            "Date.Full",
            "Station.City",
            "Station.Code",
            "Station.Location",
            "Station.State",
        ]
        if column in x:
            raise Exception("Cannot find max of these columns")
        maxval = df[column].max()
        df2 = df[df[column] == maxval]
        df3 = df2[prin]
        if export:
            df3.to_csv(export, index=False)
        else:
            print(df3)

    def min_value(self, df, column, prin, export):
        x = [
            "Date.Full",
            "Station.City",
            "Station.Code",
            "Station.Location",
            "Station.State",
        ]
        if column in x:
            raise Exception("Cannot find max of these columns")
        minval = df[column].min()
        df2 = df[df[column] == minval]
        df3 = df2[prin]
        if export:
            df3.to_csv(export, index=False)
        else:
            print(df3)

    def max_value1(self, df, column):
        x = [
            "Date.Full",
            "Station.City",
            "Station.Code",
            "Station.Location",
            "Station.State",
        ]
        if column in x:
            raise Exception("Cannot find max of these columns")
        maxval = df[column].max()
        print(maxval)
        return maxval

    def min_value1(self, df, column):
        x = [
            "Date.Full",
            "Station.City",
            "Station.Code",
            "Station.Location",
            "Station.State",
        ]
        if column in x:
            raise Exception("Cannot find max of these columns")
        minval = df[column].min()
        print(minval)
        return minval

    def mean_value(self, df, prin, export):
        x = [
            "Date.Full",
            "Station.City",
            "Station.Code",
            "Station.Location",
            "Station.State",
        ]
        for i in x:
            if i in prin:
                raise Exception("Cannot find mean of these columns")
        df1 = df.describe()
        df2 = df1[prin]
        descriptors_to_drop = ["count", "min", "std", "25%", "50%", "75%", "max"]
        df3 = df2.drop(descriptors_to_drop)
        if export:
            df3.to_csv(export, index=False)
        else:
            mean_values = []
            print(df3)
            for i in prin:
                mean_value = df3.loc["mean", i]
                mean_values.append(mean_value)
            return tuple(mean_values)
    
    def print_table(self,df,prin,export):
        if export:
            df1=df[prin]
            df1.to_csv(export,index=False)
        else:
            print(df[prin])


def Argfunc():
    parser = Par()
    args = parser.parser.parse_args()
    df = parser.file_validation(args.file)
    export = parser.export_validation(args.export)
    df1 = parser.range_validation(args.range, df)
    if df1 is not False:
        df = df1
    column = parser.column_validation(args.column, df)
    prin = parser.print_validation(args.pr, df)
    if (args.max and args.mean) or (args.max and args.min) or (args.mean and args.max):
        raise Exception("Use only one of max, min and mean")
    if args.max:
        if args.pr:
            parser.max_value(df, column, prin, export)
        else:
            parser.max_value1(df, column)
    if args.min:
        if args.pr:
            parser.min_value(df, column, prin, export)
        else:
            parser.min_value1(df, column)
    if args.mean:
        if args.pr:
            parser.mean_value(df, prin, export)
        else:
            raise Exception("please give --prin collums")
    if args.pr:
        if((not args.min) and (not args.max) and (not args.mean)):
            parser.print_table(df,prin,export)


# Main Function
if __name__ == "__main__":
    Argfunc()
