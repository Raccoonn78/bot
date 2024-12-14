import functools
import csv
from functools import wraps

LIST_OF_ADMINS = [12345678, 87654321]

def logger_function(func):
    @wraps(func)
    def wrapped(msg, *args, **kwargs):
        user_id = msg.from_user.id
        if user_id  in LIST_OF_ADMINS:
            print(f"Несанкционированный доступ запрещен для {user_id}.")
            return
        
        
        with open('loggs.csv', 'a', encoding='utf8', newline='') as csvfile:
                fieldnames = ['action','id', 'first_name', 'last_name', 'username' , 'chat_instance']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({
                                'action':         msg.data,
                                'id':             msg.from_user.id, 
                                'first_name':     msg.from_user.first_name , 
                                'last_name':      msg.from_user.last_name , 
                                'username':       msg.from_user.username  ,
                                'chat_instance':  msg.chat_instance,
                } )
        return func(msg, *args, **kwargs)
    return wrapped