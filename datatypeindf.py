import pandas as pd
import re


def main():
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    df = pd.read_excel("datatype.xlsx")
    # print(df)
    datatypelist = []
    for column in df:
        specialcharacterlist = []
        if all(isinstance(x, int) for x in df[column].tolist()):
            print('data type is integer', df[column].tolist())
            datatypelist.append('INTEGER')
        elif all(isinstance(x, float) for x in df[column].tolist()):
            print('data type is decimal', df[column].tolist())
            datatypelist.append('DECIMAL')
        # first check if all col values are string then check for alphanumeric,else check for special character
        elif all(isinstance(x, str) for x in df[column].tolist()):
            if any([bool(re.search(r'\d', x)) for x in df[column].tolist()]):
                datatypelist.append('ALPHANUMERIC')
            else:
                for entry in df[column].tolist():
                    if not (regex.search(entry) is None):
                        specialcharacterlist.append(True)
                    else:
                        specialcharacterlist.append(False)
                if all(specialcharacterlist):
                    print('data type is Special character', df[column].tolist())
                    datatypelist.append('SPECIAL Character')
                else:
                    print('data type is varchar', df[column].tolist())
                    datatypelist.append('VARCHAR')
        elif any(isinstance(x, str) for x in df[column].tolist()):
            print('data type is varchar', df[column].tolist())
            datatypelist.append('VARCHAR')
    df.loc[len(df)] = datatypelist
    print(df)
    df.to_excel("output.xlsx", index=False)


if __name__ == '__main__':
    main()
