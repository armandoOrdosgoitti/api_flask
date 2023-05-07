import mysql.connector
mysql = mysql.connector.connect(host = 'localhost',user = 'root',password = '', database = 'api_flask')
cursor = mysql.cursor()
cursor.execute('select * FROM datos')
resultados = cursor.fetchall()
respuesta = []

for resultado in resultados:
    sql = {"id":resultado[0],"nombre":resultado[1],"apellido":resultado[2],"edad":resultado[3],"sexo":resultado[4],"nacionalidad":resultado[5],"profecion":resultado[6]}
    i = respuesta.append(sql)
