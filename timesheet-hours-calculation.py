import pandas as pd
from openpyxl import load_workbook


def hours_calculation(file_path):
    """skip first 7 rows which is not required for time calculation"""
    df = pd.read_excel(file_path, na_values=['NA'],
                       skiprows=7)
    # print(df)
    """drop two columns Project/Initiative ID & Project /Initiative Name"""
    new_df = df.drop(['Project /Initiative ID', 'Project /Initiative Name'], axis=1)
    print(new_df)
    total_number_hours = new_df.sum(numeric_only=True).sum()
    print(total_number_hours)
    """adding total hours in same excel"""
    wb = load_workbook(file_path)
    work_sheet = wb.active  # Get active sheet
    work_sheet.append(['Total Working Hours', total_number_hours])
    wb.save(file_path)

    # col_list = [col for col in new_df]
    # print(col_list)
    # for col in col_list:
    #     print(new_df[col])


if __name__ == '__main__':
    """Modify the file path before executing the script"""
    file_path = "C:\\Users\\learning\\Resource Time Tracking Manisha Singh.xlsx"
    hours_calculation(file_path)
