import duckdb
import os
import subprocess

# Delete the existing loan.db if it exists
database_path = 'loan.db'
if os.path.exists(database_path):
    os.remove(database_path)

cursor = duckdb.connect("loan.db")


cursor.execute("""CREATE TABLE loans AS SELECT * FROM read_csv('data/loan_dataset.csv',
               header=True,
               columns = {
               'CustomerID':'INTEGER',
               'LoanAmount':'INTEGER',
               'LoanTerm':'INTEGER',
               'InterestRate':'FLOAT',
               'ApprovalStatus':'STRING'
               })
""")

cursor.execute("""CREATE TABLE customers AS SELECT * FROM read_csv('data/customer_data.csv',
               header=True,
               columns = {
               'CustomerID':'INTEGER',
               'Name':'STRING',
               'Surname':'STRING',
               'Age':'INTEGER',
               'Gender':'STRING',
               'Income':'INTEGER',
               'Region':'STRING'
               })
""")

cursor.execute("""CREATE TABLE credit AS SELECT * FROM read_csv('data/credit_data.csv',
               header=True,
               columns = {
               'CustomerID':'INTEGER',
               'CreditScore':'INTEGER',
               'CustomerClass':'STRING'
               })
""")

cursor.execute("""CREATE TABLE repayments AS SELECT * FROM read_csv('data/Loan_Repayments.csv',
               header=True,
               columns = {
               'RepaymentID':'INTEGER',
               'RepaymentDate':'TIMESTAMP',
               'Amount':'INTEGER',
               'CustomerID':'INTEGER',
               'TimeZone' : 'String'
               })
""")


cursor.execute("""CREATE TABLE months AS SELECT * FROM read_csv('data/Months.csv',
               header=True,
               columns = {
               'MonthID':'INTEGER',
               'MonthName':'STRING',
               })
""")

cursor.close()

