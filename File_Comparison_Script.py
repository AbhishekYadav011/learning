import pandas as pd
import sys
import os


def whitespace_remover(dataframe):
    for i in dataframe.columns:
        if dataframe[i].dtype == 'object':
            dataframe[i] = dataframe[i].map(str.strip)
        else:
            pass


def file_comparision():
    filelist1 = [f1 for f1 in os.listdir(os.curdir + r'\File_1')]
    print(filelist1)
    filelist2 = [f2 for f2 in os.listdir(os.curdir + r'\File_2')]
    print(filelist2)
    for f1 in filelist1:
        for f2 in filelist2:
            if f1[-4:] == f2[-4:] == '.txt':
                seperator = input("Enter separator type")
                old = pd.read_csv(os.curdir + '\\File_1\\' + f1, sep=seperator)
                old.columns = old.columns.str.replace(' ', '')
                old = old.applymap(str)
                new = pd.read_csv(os.curdir + '\\File_2\\' + f2, sep=seperator)
                new.columns = new.columns.str.replace(' ', '')
                new = new.applymap(str)

            if f1[-4:] == f2[-4:] == '.csv':
                old = pd.read_csv(os.curdir + '\\File_1\\' + f1, sep=',')
                old.columns = old.columns.str.replace(' ', '')
                old = old.applymap(str)
                new = pd.read_csv(os.curdir + '\\File_2\\' + f2, sep=',')
                new.columns = new.columns.str.replace(' ', '')
                new = new.applymap(str)
                print("Comparison script started......")
            if f1[-5:] == f2[-5:] == '.xlxs':
                old = pd.read_excel(os.curdir + '\\File_1\\' + f1, na_values=['NA'])
                new = pd.read_excel(os.curdir + '\\File_2\\' + f2, na_values=['NA'])
            whitespace_remover(old)
            whitespace_remover(new)
    Col1 = list(old.columns)
    Col2 = list(new.columns)
    # old.columns[old.dtypes==object]
    old = old.apply(lambda x: x.fillna("NA"))
    # new.columns[new.dtypes==object]
    new = new.apply(lambda x: x.fillna("NA"))
    old.replace('0', "NA").replace('0.00', "NA")
    new.replace('0', "NA").replace('0.00', "NA")
    Report = open(os.curdir + 'Report.txt', "w+")
    Report.write("==============================FILE COMPARISON REPORT========================\n")
    Report.write("FILES USED FOR COMPARISON:" + '\n')
    Report.write("File 1: " + str(filelist1) + '\n')
    Report.write("File 2: " + str(filelist2) + '\n\n')
    if Col1 == Col2:
        Input = input("Enter key column Name on which you want to compare files separated by , for multiple columns :")
        Key = Input.split(',')
        # Key = Input()
        Report.write("==============================KEY USED FOR COMPARISON=======================\n")
        if len(Key) == 1:
            Report.write("Key: " + str(Key) + '\n')
        if len(Key) > 1:
            Report.write("Composite Key:" + str(Key) + '\n')
        Report.write("=============================================================================\n")
        Report.write("COLUMN COMPARISON:PASS" + '\n')
        Report.write("COLUMN COUNT IN 1st FILE" + ':' + str(len(old.columns)) + '\n')
        Report.write("COLUMN COUNT IN 2st FILE" + ':' + str(len(new.columns)) + '\n')
        Report.write("Column Difference" + ':' + str(abs(len(old.columns) - len(new.columns))) + '\n')
    elif Col1 != Col2:
        Input = input("Enter key column Name on which you want to compare files separated by , for multiple columns :")
        Key = Input.split(',')
        # Key = Input()
        Report.write("==============================KEY USED FOR COMPARISON========================\n")
        if len(Key) == 1:
            Report.write("Key: " + str(Key) + '\n')
        if len(Key) > 1:
            Report.write("Composite Key:" + str(Key) + '\n')
        Report.write("=============================================================================\n")
        Report.write('COLUMN COMPARISON:FAIL \n')
        Report.write("Number of columns in 1st File" + ':' + str(len(old.columns)) + '\n')
        Report.write("Number of columns in 2nd File" + ':' + str(len(new.columns)) + '\n')
        Report.write("Column Difference" + ':' + str(abs(len(old.columns) - len(new.columns))) + '\n')
        Report.write("Columns in : File 1" + " not in : File 2"  ' :' + ', '.join(list(set(Col1) - set(Col2))) + '\n')
        Report.write("Columns in : File 2" + " not in : File 1" + ' :' + ', '.join(list(set(Col2) - set(Col1))) + '\n')
    if any(item in Key for item in list(set(Col1) - set(Col2))):
        Report.write("Comparison Fails as column not part of File2 is taken as Key." + '\n')
        Report.close()
        sys.exit("Script exit as column not part of File2 is taken as Key")
    elif any(item in Key for item in list(set(Col2) - set(Col1))):
        Report.write("Comparison Fails as column not part of File1 is taken as Key." + '\n')
        Report.close()
        sys.exit("Script exit as column not part of File1 is taken as Key")
    elif not ((set(Key).issubset(set(Col1))) & (set(Key).issubset(set(Col2)))):
        Report.write("Comparison Fails as column taken as key not  part of File1 & File2. " + '\n')
        Report.close()
        sys.exit("Script exit as as column taken as key not  part of File1 & File2")
    if len(Key) > 1:
        old['Key'] = old[Key].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
        new['Key'] = new[Key].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    else:
        old['Key'] = old[Key]
        new['Key'] = new[Key]
    if any(new['Key'].duplicated() & old['Key'].duplicated()):
        Key_dup1 = old[old['Key'].isin(old['Key'][old['Key'].duplicated()])]
        Key_dup2 = new[new['Key'].isin(new['Key'][new['Key'].duplicated()])]
        Report.write("Comparison Fails as Key column contains duplicate records in File1 for below key \n" + str(
            Key_dup1['Key'].unique()) + '\n')
        Report.write("Comparison Fails as Key column contains duplicate records in File2 for below key \n" + str(
            Key_dup2['Key'].unique()) + '\n')
        Report.close()
        sys.exit("Script exit as Key column contains duplicate records in File1 & File2")
    if any(old['Key'].duplicated()):
        Key_dup = old[old['Key'].isin(old['Key'][old['Key'].duplicated()])]
        Report.write("Comparison Fails as Key column contains duplicate records in File1 for below key \n" + str(
            Key_dup['Key'].unique()) + '\n')
        Report.close()
        sys.exit("Script exit as Key column contains duplicate records in File1")
    if any(new['Key'].duplicated()):
        Key_dup = new[new['Key'].isin(new['Key'][new['Key'].duplicated()])]
        Report.write("Comparison Fails as Key column contains duplicate records in File2 for below key \n" + str(
            Key_dup['Key'].unique()) + '\n')
        Report.close()
        sys.exit("Script exit as Key column contains duplicate records in File2")

    if len(list(set(Col1) - set(Col2))) != 0:
        old.drop(list(set(Col1) - set(Col2)), axis=1, inplace=True)
        Col1 = list(old.columns)
    if len(list(set(Col2) - set(Col1))) != 0:
        new.drop(list(set(Col2) - set(Col1)), axis=1, inplace=True)
        Col2 = list(new.columns)
    old['version'] = "old"
    new['version'] = "new"
    old_pol_no_all = set(old['Key'])
    new_pol_no_all = set(new['Key'])
    dropped_pol_no = old_pol_no_all - new_pol_no_all
    added_pol_no = new_pol_no_all - old_pol_no_all
    all_data = pd.concat([old, new], ignore_index=True)
    chg = all_data.drop_duplicates(subset=Col1, keep='last')
    duplicate_Key = chg[chg['Key'].duplicated() == True]['Key'].tolist()
    dup = chg[chg['Key'].isin(duplicate_Key)]
    chg_new = dup[(dup["version"] == "new")]
    chg_old = dup[(dup["version"] == "old")]
    chg_new = chg_new.drop(['version'], axis=1)
    chg_old = chg_old.drop(['version'], axis=1)
    chg_new.set_index(Key, inplace=True)
    chg_old.set_index(Key, inplace=True)

    df_all_chg = pd.concat([chg_old, chg_new], sort=True, axis='columns', keys=['old', 'new'], join='outer')
    writer = pd.ExcelWriter("FINAL_COMPARISON_REPORT.xlsx")
    output_columns = Col1
    df_removed = chg[chg['Key'].isin(dropped_pol_no)]
    df_added = chg[chg['Key'].isin(added_pol_no)]

    def report_diff(x):
        return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)

    if not (chg_old.empty & chg_new.empty):
        df_all_chg = df_all_chg.swaplevel(axis='columns')[chg_new.columns[0:]]
        df_chg = df_all_chg.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))
        df_chg = df_chg.reset_index()
        df_diff_count = (
            df_chg.select_dtypes(object).applymap(lambda x: '--->' in x if isinstance(x, str) else False).sum())
        df_diff_count = df_diff_count[df_diff_count > 0].dropna()
        df_diff_count.to_excel(writer, "Column_Count_diff")
        df_chg = df_chg.reindex(columns=['Key'] + output_columns)
        df_chg.to_excel(writer, sheet_name='Changed', index=False, columns=['Key'] + output_columns)
        workbook = writer.book
        worksheet = writer.sheets['Changed']
        format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                       'font_color': '#9C0006'})
        worksheet.conditional_format(1, 1, len(df_chg), len(output_columns),
                                     {'type': 'text',
                                      'criteria': 'containing',
                                      'value': '--->',
                                      'format': format1})
    df_chg_empty = pd.DataFrame(columns=['Key'] + output_columns)
    df_diff_count_empty = pd.DataFrame(columns=['   ', 0])
    df_diff_count_empty.to_excel(writer, index=False, sheet_name="Column_Count_diff")
    df_chg_empty.to_excel(writer, index=False, sheet_name='Changed')
    ##################################################################################
    df_removed.to_excel(writer, "Present_In_File1", index=False, columns=['Key'] + output_columns)
    df_added.to_excel(writer, "Present_In_File2", index=False, columns=['Key'] + output_columns)
    writer.save()
    if str(len(old)) == str(len(new)):
        Report.write("=============================================================================\n")
        Report.write("ROW COUNT COMPARISON:PASS" + '\n')
        Report.write('RowCount of 1st File :' + str(len(old)) + '\n')
        Report.write('RowCount of 2nd File :' + str(len(new)) + '\n')
        Report.write('Row Difference :' + str(abs(len(old) - len(new))) + '\n')
    else:
        Report.write("=============================================================================\n")
        Report.write("ROW COUNT COMPARISON:FAIL"'\n')
        Report.write('RowCount of 1st File :' + str(len(old)) + '\n')
        Report.write('RowCount of 2nd File :' + str(len(new)) + '\n')
        Report.write('Row Difference :' + str(abs(len(old) - len(new))) + '\n')
    if chg_old.empty & chg_new.empty & df_removed.empty & df_added.empty:
        Report.write("=============================================================================\n")
        Report.write("DATA COMPARISON : PASS" + '\n')
    else:
        Report.write("=============================================================================\n")
        Report.write("DATA COMPARISON : FAIL" + '\n')
    Report.close()


if __name__ == '__main__':
    file_comparision()
