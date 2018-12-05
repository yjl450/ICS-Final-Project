import chat_client_class as cmclass

def log_in_botton(user_name,label):
    # copied from chat_cmdl_client
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()
    # end of copy
    user = cmclass.Client(args)
    # initial the chat manually
    user.init_chat()
    if user_name == '':
        label.setText('please enter a valid user name')
        logged = False
    else:
        user.console_input.append(user_name)
        login_status = user.login()
        if login_status:
            logged = True
        else:
            text = user.system_msg
            label.setText(text)
            logged = False
    return logged,user


def send_button(user,text):
    user.console_input.append(text)
    user.proc()
    message = user.output()
    return message


