import configparser

config_file = configparser.ConfigParser()
config_file.add_section("SMTPlogin")

config_file.set("SMTPlogin", "sender_address", "rathoddharmaraj2512@gmail.com")
config_file.set("SMTPlogin", "receiver_address", "rathoddharmaraj2512@gmail.com")
config_file.set("SMTPlogin", "mailtrap_user", "f8935d22458748")
config_file.set("SMTPlogin", "mailtrap_password", "7df6a7d275bbbb")

with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)

print("Config file 'configurations.ini' created")
