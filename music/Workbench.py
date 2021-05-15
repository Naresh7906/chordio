import pyodbc


class Workbench:
    def __init__(self,dbname,user="root",host="localhost",password="root"):
        self.databaseName=dbname
        self.user=user
        self.host=host
        self.password=password
        self.connectToDB()

    def connectToDB(self):
        self.conn=pyodbc.connect(
            'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
            'SERVER='+self.host+';'
            'DATABASE='+self.databaseName+';'
            'UID='+self.user+';'
            'PWD='+self.password+';'
            'charset=utf8mb4;'
        )
        

    def createTable(self,tablename,column={}):
        if(len(column)==0):
            print("Invalid Input")
        else:
            create="CREATE TABLE IF NOT EXISTS "+ tablename +"("
            j=0
            for i in column:
                
                if(j<len(column)-1):
                    create+=i + " " 
                    create+=column[i]
                    create+=','
                else:
                    create+=i + " " 
                    create+=column[i]
                j+=1
            create+=")"

            print(create)
        cursor = self.conn.cursor()
        cursor.execute(create)
        self.conn.commit()

    def insertInto(self,insert):

        print(insert)
        cursor = self.conn.cursor()
        cursor.execute(insert)
        self.conn.commit()

    
    
    def selectFromTable(self,tablename,attribute=[],where={},key=[]):
        if len(attribute)==0:
            users="SELECT * FROM "+tablename
        else:
            users="SELECT "
            for i in range(len(attribute)):
                if(i<len(attribute)-1):
                    users+=attribute[i]
                    users+=','
                else:
                    users+=attribute[i]
            users+=" FROM "+tablename

       
        if(len(where)>0):
            users+=' WHERE '
            j=0
            for i in where:
                if(j<len(where)-1):
                    users+="`"+i+"`"
                    users+=" = '"
                    users+=where[i]
                    users+="' "+key+" "
                else:
                    users+="`"+i+"`"
                    users+=" = '"
                    users+=where[i]
                    users+="' "
                j+=1
        
        cursor = self.conn.cursor()
        cursor.execute(users)
        result=cursor.fetchall()
        for i in result:
            print(i)


    def updateTable(self,tablename,attribute=[],where={},key=[]):
        update="UPDATE "+tablename+" SET "
        if(len(attribute)==0):
            print("Invalid input")

        elif(len(attribute)>0):
            j=0
            for i in attribute:
                if(j<len(attribute)-1):
                    update+=i
                    update+=" = '"
                    update+=attribute[i]
                    update+="' , "
                else:
                    update+=i
                    update+=" = '"
                    update+=attribute[i]
                    update+="' "
                j+=1
        
            if(len(where)>0):
                update+='WHERE '
                j=0
                for i in where:
                    if(j<len(where)-1):
                        update+="`"+i+"`"
                        update+=" = '"
                        update+=where[i]
                        update+="' "+key+" "
                    else:
                        update+="`"+i+"`"
                        update+=" = '"
                        update+=where[i]
                        update+="' "
                    j+=1
            print(update)

            cursor = self.conn.cursor()
            cursor.execute(update)
            self.conn.commit()


    def deleteTable(self,tablename, where={}, key=[]):
        if(len(where)==0):
            delete="DELETE FROM "+tablename 
        
        
        elif len(where)>0:
            delete+=" WHERE "
            j=0       
            for i in where:
                if(j<len(where)-1):
                    delete+="`"+i+"`"
                    delete+="='"
                    delete+= where[i]
                    delete+="' " +key+" "
                else:
                    delete+="`"+i+"`"
                    delete+="='"
                    delete+= where[i]
                    delete+="'"
                j+=1
                
        print(delete)
        self.conn.commit()
            

'''a=Workbench('music_system')


a.selectFromTable('songs')

a.updateTable('student')

a.deleteTable('student')

col={'A' : 'int', 'B': 'varchar(20)'}
a.createTable('ASD',col)'''


