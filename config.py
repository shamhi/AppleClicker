from dotenv import dotenv_values

env = dotenv_values()

class Config:
    TOKEN = env.get('TOKEN')
    PORT = env.get('PORT')
