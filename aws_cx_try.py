"""
Simple example of using DbCon.
Run from AWS "production" workspace.
Gets enabled hub jobs from E10/Staging hub.
Uses cx_Oracle and direct database connection.
"""

from dbcon_multi import DbCon

database = "!lh10xwbgmxq6h2j.cptix4mlxjrs.eu-west-2.rds.amazonaws.com,hub"
username = raw_input("Hub username:")
password = raw_input("Hub password (will show!):")

hub_con = DbCon(username, password, database)
hub_con.runsql("select process_code from hub_processes where enabled='Y'")
hub_con.close()

print hub_con.results
print hub_con.errors
