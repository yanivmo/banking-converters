import excel2csv as exl


def discount_conversion(from_file, to_file):
    """
    Convert an Excel file containing checking account transaction, as supplied by Israel Discount Bank.
    Currently the bank's web site supports only exports in Excel SpreadsheetML format.
    """
    namespaces = {'x': 'urn:schemas-microsoft-com:office:spreadsheet'}
    start_cell = 'תנועות אחרונות:'
    end_cell = 'הודעה'

    # Select all the rows between a row containing a cell with `start_cell` text
    # until the row containing a cell with `end_cell` text
    data_rows_xpath = ('/x:Workbook/x:Worksheet/x:Table/'
                       'x:Row[x:Cell/x:Data[text()="{}"]]/'
                       'following-sibling::x:Row[following::x:Row/x:Cell/x:Data[text()="{}"]]'
                       ).format(start_cell, end_cell)
    data = exl.spreadsheetml_to_list(from_file, data_rows_xpath, namespaces)

    # This is the expected table header. Ensure it is as expected to get an exception if
    # the bank suddenly changes the table structure
    expected_columns = ['תאריך הפעולה', 'יום ערך', 'תיאור הפעולה', 'אסמכתה', 'זכות / חובה', 'יתרה משוערת']
    assert data[0] == expected_columns

    exl.list_to_csv(data[1:], to_file, drop_columns=[1, 3, 5])
    print('Converted', len(data)-1, 'rows')


if __name__ == '__main__':
    discount_conversion('tests/discount2.xls', 'output.csv')
