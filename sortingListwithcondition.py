import re

testList = ['FUND-MATURITY-DUE-DTE._1',
            'FUND-MATURITY-DUE-DTE._2 ',
            'FUND-MATURITY-DUE-DTE._3 ',
            'FUND-MATURITY-DUE-DTE._4 ',
            'FUND-MATURITY-DUE-DTE._5', 'FUND-MATURITY-CCYY_1 PIC 9(04).',
            'FUND-MATURITY-CCYY_2 PIC 9(04).',
            'FUND-MATURITY-CCYY_3 PIC 9(04).',
            'FUND-MATURITY-CCYY_4 PIC 9(04).',
            'FUND-MATURITY-CCYY_5 PIC 9(04).', 'FUND-MATURITY-MM_1 PIC 9(02).',
            'FUND-MATURITY-MM_2 PIC 9(02).',
            'FUND-MATURITY-MM_3 PIC 9(02).',
            'FUND-MATURITY-MM_4 PIC 9(02).',
            'FUND-MATURITY-MM_5 PIC 9(02).']

testList.sort(key=lambda test_string: list(
    map(int, re.findall(r'\d+', test_string)))[0])

print(testList)
