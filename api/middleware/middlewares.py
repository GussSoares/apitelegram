

def filter_data(data: dict):
    redirect_data = {}
    message = data.get('message')

    if content := message.get('text'):
        redirect_data.update({
            'chat_id': message.get('chat').get('id'),
            'text': content.get('text'),
            'url': '/telegram/sendMessage',
        }) 
    elif content := message.get('photo'):
        redirect_data.update({
            'chat_id': message.get('chat').get('id'),
            'file_id': content[-1].get('file_id'),
            'url': '/telegram/sendPhoto',
        })

    return redirect_data
