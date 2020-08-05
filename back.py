import cx_Oracle
def cred_check(a,b,c,d):
    apple = a+'/'+b+'@'+c+'/'+d
    conn=cx_Oracle.connect(apple)
    if conn :
        return 1 # returns 1 if credentials work
    else :
        return 0 # returns 0 if credentials don't work
    conn.close()
