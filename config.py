"""Flask configuration."""

#Main Config
TESTING = True
DEBUG = False
#FLASK_ENV = 'development'
SECRET_KEY = 'Sit@rA_gOlD'
SECURITY_PASSWORD_SALT = 'Sit@rA_gOlD_p285f'
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"

#MySQL database configuration
MYSQL_HOST = 'chatterbox-do-user-14126773-0.b.db.ondigitalocean.com'
MYSQL_PORT = '25060'
MYSQL_USER = 'doadmin'
MYSQL_PASSWORD = 'AVNS_SqedU0rkh1q5DWStOMp'
MYSQL_DB = "chatterbox"

#App password for gmail account
MAIL_SENDER = 'ahmadd42@gmail.com'
MAIL_APP_PASSWORD = 'tyrhysfknxnxfbew'