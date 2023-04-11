import pandas as pd

old = pd.read_excel("File_1.xlsx", 'Sheet1', na_values=['NA'])
new = pd.read_excel("File_2.xlsx", 'Sheet1', na_values=['NA'])
old['version'] = "old"
new['version'] = "new"
old_pol_no_all = set(old['POL_NUMBER'])
new_pol_no_all = set(new['POL_NUMBER'])
print(old_pol_no_all)
print(new_pol_no_all)
dropped_pol_no = old_pol_no_all - new_pol_no_all
added_pol_no = new_pol_no_all - old_pol_no_all
# Next we join all the data together and get a clean list of unique data and keep all changed rows by using drop_duplicates
all_data = pd.concat([old, new], ignore_index=True)
changes = all_data.drop_duplicates(subset=["POL_NUMBER",
                                           "PLAN_CODE", "ABC",
                                           "DEF"], keep='last')
# figure out which Poll numbers have duplicate entries,only those entries will have changed value
dupe_pol_no = changes[changes['POL_NUMBER'].duplicated() == True]['POL_NUMBER'].tolist()
dupes = changes[changes["POL_NUMBER"].isin(dupe_pol_no)]
print(dupes)
# Now we break out the old and new data, remove the unnecesary version column and set the poll number as the index.
# Pull out the old and new data into separate dataframes
change_new = dupes[(dupes["version"] == "new")]
change_old = dupes[(dupes["version"] == "old")]
# Drop the temp columns - we don't need them now
change_new = change_new.drop(['version'], axis=1)
change_old = change_old.drop(['version'], axis=1)
# Index on the Poll numbers
change_new.set_index('POL_NUMBER', inplace=True)
change_old.set_index('POL_NUMBER', inplace=True)

# Combine all the changes together
df_all_changes = pd.concat([change_old, change_new],
                           axis='columns',
                           keys=['old', 'new'],
                           join='outer')


# Define the diff function to show the changes in each field
def report_diff(x):
    return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)


# We now use the swaplevel function to get the old and new columns next to each other
df_all_changes = df_all_changes.swaplevel(axis='columns')[change_new.columns[0:]]
# print(df_all_changes)
# The final tricky command is to use a groupby on the columns then apply,
# our custom report_diff function to compare the two corresponding columns to each other.
df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))
df_changed = df_changed.reset_index()
print(df_changed)
# Finally all poll number which is not present in both the excel
df_removed = changes[changes["POL_NUMBER"].isin(dropped_pol_no)]
df_added = changes[changes["POL_NUMBER"].isin(added_pol_no)]
# We can output everything to an Excel file
output_columns = ["POL_NUMBER", "PLAN_CODE", "ABC", "DEF"]
writer = pd.ExcelWriter("Final_Report.xlsx")
df_changed.to_excel(writer, "changed", index=False, columns=output_columns)
df_removed.to_excel(writer, "File1", index=False, columns=output_columns)
df_added.to_excel(writer, "File2", index=False, columns=output_columns)
writer.save()
