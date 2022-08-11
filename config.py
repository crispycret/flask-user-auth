import os

# from dotenv import load_dotenv
# load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

_summary_ = """
    The Configuration class is used to configure and secure the application.
    
    SECRET_KEY - Application secret key that needs to be generated by the application developer.
                 This parameter is used to sign and read authentication requests.
        [+] Build a tool to help the application developer create and manage SECRET_KEY generation. 
     
"""
class Configuration (object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'default.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    