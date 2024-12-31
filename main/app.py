from config.deb_config import ConnectToDb

if __name__ == '__main__':
    db_obj=ConnectToDb()
    db_obj.create_connection()