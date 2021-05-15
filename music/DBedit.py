import mysql.connector
import datetime


class DBconn:
    def __init__(self):

        self.select = "select * from "
        self.insert_ar = "insert into artist(artist_name,artisuuuuuuuuut_origin) VALUES ((%s),(%s))"
        self.insert_al = "insert into album(album_name,artist_id,album_date,album_art) VALUES ((%s),(%s),(%s),(%s))"
        self.insert_sn = "insert into songs(song_name,song_date,album_id,artist_id) VALUES ((%s),('%s'),(%s),(%s))"
        self.update_ar = "update artist set artist_name = %s , artist_origin = %s where artist_id = %s"
        self.update_al = "update album set album_name = %s , artist_id = %s and album_date = %s where album_id = %s"
        self.update_sn = "update artist set artist_name = %s , artist_origin = %s where artist_id = %s"
        self.find_ar = "select * from artist where artist_name LIKE "
        self.find_al = "select * from album where album_name LIKE "
        self.find_sn = "select * from song where song_name LIKE "
        self.ar = "artist"
        self.al = "album"
        self.sn = "songs"
        self.mydb = self.connect()
        self.insert_ur = "INSERT INTO user(f_name,l_name,email_address,user_password) values((%s),(%s),(%s),(%s))"
        self.check_ur = "Select * from user where email_address = (%s)"
        self.get_ur = "Select * from user where user_password = (%s) and email_address = (%s)"
        self.mydb = self.connect()

    def connect(self):

        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user="chordio",
            password="chordio",
            database="chordio"
        )
        return mydb

    def show_artist(self):

        mycursor = self.mydb.cursor()
        mycursor.execute(self.select + self.ar)
        myresult = mycursor.fetchall()
        return myresult

    def show_album(self):

        mycursor = self.mydb.cursor()
        mycursor.execute(self.select + self.al)
        myresult = mycursor.fetchall()
        return myresult

    def show_songs_con(self):

        mycursor = self.mydb.cursor()
        mycursor.execute(self.select + self.sn)
        myresult = mycursor.fetchall()
        return myresult

    def show_songs_web(self):
        mycursor = self.mydb.cursor()
        stat = "select song.song_name,album.album_name,artist.artist_name,album.album_art,song.song_id from song,album,artist where song.album_id = album.album_id and song.artist_id = artist.artist_id"
        mycursor.execute(stat)
        myresult = mycursor.fetchall()
        return myresult

    def show_album_web(self):
        mycursor = self.mydb.cursor()
        stat = "select album.album_name,album.album_date,artist.artist_name,album.album_art from album,artist where album.artist_id = artist.artist_id"
        mycursor.execute(stat)
        myresult = mycursor.fetchall()
        return myresult    

    def insert_artist(self):

        mycursor = self.mydb.cursor()
        name = input("Enter artist name: ")
        origin = input("Enter artist origin: ")
        parameters = [name, origin]
        mycursor.execute(self.insert_ar, parameters)
        self.mydb.commit()

    def insert_album(self):

        mycursor = self.mydb.cursor()
        name = input("Enter album name: ")
        artist = int(input("Enter artist id: "))
        date = input("Enter album date(dd/mm/yyyy): ")
        edate = datetime.datetime.strptime(date, "%d/%m/%Y")
        parameters = [name, artist, edate]
        mycursor.execute(self.insert_al, parameters)
        self.mydb.commit()

    def insert_song(self):

        mycursor = self.mydb.cursor()
        name = input("Enter song name: ")
        date = input("Enter song date(dd/mm/yy): ")
        album = int(input("Enter album id: "))
        artist = int(input("Enter artist id: "))
        edate = datetime.datetime.strptime(date, "%d/%m/%Y")
        parameters = [name, edate, album, artist]
        mycursor.execute(self.insert_sn, parameters)
        self.mydb.commit()

    def update_artist(self):

        mycursor = self.mydb.cursor()
        id = int(input("Enter artist id to be updated: "))
        name = input("Enter artist name: ")
        origin = input("Enter artist origin: ")
        parameters = [name, origin, id]
        mycursor.execute(self.update_ar, parameters)
        self.mydb.commit()

    def update_album(self):

        id = int(input("Enter album id to be updated: "))
        mycursor = self.mydb.cursor()
        name = input("Enter album name: ")
        artist = int(input("Enter artist id: "))
        date = input("Enter album date(dd/mm/yyyy): ")
        edate = datetime.datetime.strptime(date, "%d/%m/%Y")
        parameters = [name, artist, edate, id]
        mycursor.execute(self.update_al, parameters)
        self.mydb.commit()

    def update_song(self):

        id = int(input("Enter song id to be updated: "))
        mycursor = self.mydb.cursor()
        name = input("Enter song name: ")
        date = input("Enter song date(dd/mm/yy): ")
        album = int(input("Enter album id: "))
        artist = int(input("Enter artist id: "))
        edate = datetime.datetime.strptime(date, "%d/%m/%Y")
        parameters = [name, edate, album, artist, id]
        mycursor.execute(self.update_sn, parameters)
        self.mydb.commit()

    def find_artist(self,id):
        parameters = "'%"+id+"%'"
        mycursor = self.mydb.cursor()
        mycursor.execute(self.find_ar + parameters)
        myresult = mycursor.fetchall()
        return myresult

    def find_album(self,id):
        parameters = "'%"+id+"%'"
        mycursor = self.mydb.cursor()
        mycursor.execute(self.find_al + parameters)
        myresult = mycursor.fetchall()
        return myresult

    def find_songs_con(self,id):
        parameters = "'%"+id+"%'"
        mycursor = self.mydb.cursor()
        mycursor.execute(self.find_sn + parameters)
        myresult = mycursor.fetchall()
        return myresult

    def find_songs_web(self,id):
        parameters = "'%"+id+"%'"
        print(parameters)
        mycursor = self.mydb.cursor()
        stat = "select song.song_name,album.album_name,artist.artist_name,album.album_art,song.song_id from song,album,artist where song.album_id = album.album_id and song.artist_id = artist.artist_id and song.song_name like"
        mycursor.execute(stat + parameters)
        myresult = mycursor.fetchall()
        return myresult        

    def find_all(self,id):
        parameters = "'%"+id+"%'"
        mycursor = self.mydb.cursor()
        mycursor.execute(self.find_sn + parameters)
        res1 = mycursor.fetchall()
        mycursor.execute(self.find_al + parameters)
        res2 = mycursor.fetchall()
        mycursor.execute(self.find_ar + parameters)
        res3 = mycursor.fetchall()
        myresult = res1 + res2 + res3
        return myresult

    def add_user(self,f_name,l_name,email,password):
        parameters = [f_name,l_name,email,password]
        mycursor = self.mydb.cursor()
        mycursor.execute(self.insert_ur,parameters)
        self.mydb.commit()

    def user_exist(self,email):
        mycursor = self.mydb.cursor()
        mycursor.execute(self.check_ur, [email])
        result = mycursor.fetchall()
        try : 
            if result[0]:
                return True
        except : return False

    def get_user(self,password,email):
        mycursor = self.mydb.cursor()
        parameters = [password,email]
        mycursor.execute(self.get_ur,parameters)
        result = mycursor.fetchall()
        try : 
            if result[0]:
                return True
        except : return False

    def user_data(self,email):
        mycursor = self.mydb.cursor()
        mycursor.execute("select * from user where email_address = (%s)", [email])
        result = mycursor.fetchall()
        return result

    def update_user(self,f_name,l_name,password,email):
        mycursor = self.mydb.cursor()
        parameters = [f_name,l_name,password,email]
        mycursor.execute("update user set f_name = (%s), l_name = (%s), password = (%s) where email_address = (%s)")
        mycursor.commit()        

    def delete_user(self,email):
        mycursor = self.mydb.cursor()
        mycursor.execute("delete from user where email_address = (%s)",[email])
        mycursor.commit()