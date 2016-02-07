import excel2csv as exl


def cal_conversion(from_file, to_file):
    """
    Convert an Excel file containing credit card transaction, as supplied by Cal Israel Credit Cards.
    Currently Cal's web site supports only exports in Excel XLSHTML format.
    """
    data_table_xpath = '/html/body/form/table//table'
    columns, data = exl.html_table_to_list(from_file, data_table_xpath)

    # This is the expected table header. Ensure it is as expected to get an exception if
    # the bank suddenly changes the table structure
    expected_columns = ['תאריך העסקה', 'שם בית העסק', 'סכום העסקה', '', 'סכום החיוב', '', 'פירוט נוסף']
    assert columns == expected_columns

    exl.list_to_csv(data, to_file, drop_columns=[2, 3, 5, 6])
    print('Converted', len(data), 'rows')


if __name__ == '__main__':
    cal_conversion('yaniv.xlshtml', 'output.csv')
