import datetime

color = {
    "reset": '\x1b[0m',
    "debug": '\x1b[30m',
    "error": '\x1b[41m',
    "success": '\x1b[42m',
    "warning": '\x1b[43m',
    "info": '\x1b[44m',
}

def init_logger():
    with open("logs.log", 'w') as f:
        log_info("Logger initiated")
        f.close()

def error_handle(error_type, error_place, error_message):
    if error_type == "ERROR":
        current_color = color['error']
    else:
        current_color = color['warning']

    print(f"{current_color} {error_type} {color['reset']} [{datetime.datetime.now()}] ({error_place}): {error_message}")
    with open("logs.log", 'a+') as f:
        error_type = "WARN"
        f.write(f"{datetime.datetime.now()} {error_type} ({error_place}) : {error_message}\n")
        f.close()

def log_info(log_message, message_type="INFO"):
    if message_type == "INFO":
        current_color = color['info']
    elif message_type == "DEBUG":
        current_color = color['debug']
    else:
        current_color = color['success']

    print(f"{current_color} {message_type} {color['reset']} [{datetime.datetime.now()}] : {log_message}")
    with open("logs.log", 'a+') as f:
        f.write(f"{datetime.datetime.now()} {message_type} : {log_message}\n")
        f.close()