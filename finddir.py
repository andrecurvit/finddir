# -*- coding: utf-8 -*-
import requests

dire = ["admin", "login", "php", "mysql", "livro", "access" "adm", "ADM", "admin",
        "Admin", "ADMIN", "admin.cgi", "admin.php", "admin.pl", "admin_", "admin_area",
        "admin_banner", "admin_c", "admin_index", "admin_interface", "admin_login",
        "admin_logon", "admin1", "admin2", "admin3", "admin4_account", "admin4_colon",
        "admin-admin", "admin-console", "admincontrol", "admincp", "adminhelp", "admin-interface",
        "administer", "administr8", "administracion", "administrador", "administrat", "administratie",
        "administration", "Administration", "administrator", "administratoraccounts",
        "administrators", "administrivia", "adminlogin", "adminlogon", "adminpanel", "adminpro",
        "admins", "AdminService", "adminsessions", "adminsql", "admintools", "AdminTools", "logger",
        "logging", "login", "Login", "login_db", "login_sendpass", "login1", "loginadmin", "loginflat",
        "login-redirect", "logins", "login-us", "logo", "logo_sysadmin", "logoff", "logon", "logos", "logout"]

url = input('Insira sua URL (com "/" no final): ')

print("Esse processo pode ser um pouco demorado...")

for diretorio in dire:
    r = requests.get(url + diretorio)
    if r.status_code == 200:
        print("Encontrei isto => " + diretorio)
    if r.status_code == 404:
        print("404..." + diretorio)
    if r.status_code == 403:
        print("Forbiden - 403..." + diretorio) #opcional, se nãao quiser ver os códigos de site, remover via editor.
        print("Espero ter te ajudado!")
        print("Até a próxima!")
