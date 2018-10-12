"""
Simple example of using DbCon.
Run from CZ VDI.
Gets enabled batch modules from E10/Staging CIS.
Uses pydobc and requires tnsnames.ora.
Note odbc driver name specified below.
"""

from dbcon_multi import DbCon

database = "E10DTCIS"
username = raw_input("CIS username:")
password = raw_input("CIS password (will show!):")

odbc = "Oracle in Instantclient11_1"

cis_con = DbCon(username, password, database, odbc_driver=odbc)
cis_con.runsql("select module_id from batch_modules where enabled='Y'")
cis_con.close()

print cis_con.results
print cis_con.errors
