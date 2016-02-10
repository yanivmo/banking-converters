# Financial Data Converters
Scripts to manipulate data exported form banks, credit card companies and other financial organizations.

## Usage
```
python discount_bank.py [-h] xls_file csv_file
python cal.py [-h] xls_file csv_file
```

## Background
Those who manage their finances in financing software often face the challenge of transferring the data between
the financial institutions and their software of choice. Not always the exported data is in a format that can be
easily imported. This package tries to simplify this problem. The scripts can be used as-is as executables or
imported into other Python scripts.

## Supported use cases
* [Israel Discount Bank](https://www.discountbank.co.il/) - Export checking account account into an MS Excel file, 
  convert to CSV and import into GnuCash.
* [Cal Israel Credit Cards](https://www.cal-online.co.il/) - Export monthly credit card expenses into an MS Excel file, 
  convert to CSV and import into GnuCash.

## Dependencies
* lxml
