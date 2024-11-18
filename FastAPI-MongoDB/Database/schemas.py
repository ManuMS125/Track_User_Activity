def individual_serial(user)->dict:
    return {
        'id':str(user['_id']),
        'name':user['name'],
        'location':user['location'],
        'hobby':user['hobby']
    }

def list_serial(users)->list:
    return [individual_serial(user) for user in users]