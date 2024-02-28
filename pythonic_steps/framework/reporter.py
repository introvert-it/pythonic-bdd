import re


def parse_message_args(message, func, args):
    pattern = r"{[_a-zA-Z]+}"
    message_args = re.search(r"{[_a-zA-Z]+}", message)
    function_args = func.__code__.co_varnames
    if message_args:
        for reg in message_args.regs:
            start = reg[0]
            end = reg[1]
            which_arg = function_args.index(message[start + 1:end - 1])
            return re.sub(pattern, f'"{args[which_arg]}"', message)
    return message


def chain_message(message):
    def inner(func):
        def wrapper(*args, **kwargs):
            updated_message = parse_message_args(message, func, args)

            getattr(getattr(args[0], "_scenario"), "msg_chain").append(updated_message)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return inner

