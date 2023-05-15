import mysql.connector
mysql = mysql.connector.connect(host = 'localhost',user = 'armando_dev',password = '20050962', database = 'api_flask')
cursor = mysql.cursor()
cursor.execute('select * FROM datos')
resultados = cursor.fetchall()
respuesta = []

for resultado in resultados:
    sql = {"id":resultado[0],"nombre":resultado[1],"apellido":resultado[2],"edad":resultado[3],"sexo":resultado[4],"nacionalidad":resultado[5],"profecion":resultado[6]}
    i = respuesta.append(sql)
