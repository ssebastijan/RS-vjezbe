import asyncio

def get_database_users():
    return [
        {
            "username": "mirko123",
            "email": "mirko123@gmail.com"
        },
        {
            'username': 'ana_anic',
            'email': 'aanic@gmail.com'
        },
        {
            'username': 'maja_0x', 
            'email': 'majaaaaa@gmail.com'
        },
        {
            'username': 'zdeslav032',
            'email': 'deso032@gmail.com'
        }
    ]

def get_database_user_passwords():
    return [
        {
            "username": "mirko123",
            "password": "lozinka123"
        },
        {
            'username': 'ana_anic',
            "password": "super_teska_lozinka"
        },
        {
            'username': 'maja_0x',
            "password": "s324SDFfdsj234"
        },
        {
            'username': 'zdeslav032',
            "password": "deso123"
        }
    ]

async def authentication(login_user: dict):
    await asyncio.sleep(3)
    users = get_database_users()
    for u in users:
        if u['username'] == login_user['username'] and u['email'] == login_user['email']:            
            return await authorize(u, login_user['password'])
        
    return f"Korisnik {login_user['username']} nije pronađen"


async def authorize(user: dict, password: str):
    await asyncio.sleep(2)
    database_password_users = get_database_user_passwords()

    for u in database_password_users:
        if user['username'] == u['username'] and u['password'] == password:
            return f"Korisnik {user['username']}: Autorizacija uspješna."
    
    return f"Korisnik {user['username']}: Autorizacija neuspješna."



async def main():

    login_users = [
        {
            "username": "djido_mova",
            "email": "djido_mova@gmail.com",
            "password": "12345647890"
        },
        {
            'username': 'ana_anic',
            'email': 'aanic@gmail.com',
            "password": "super_teska_lozinka"
        },
        {
            'username': 'maja_0x',
            'email': 'majaaaaa@gmail.com',
            "password": "super_teska_lozinka"
        }
    ]

    for login_user in login_users:
        print(await authentication(login_user))

asyncio.run(main())
