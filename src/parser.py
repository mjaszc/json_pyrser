tokens = {"LBRACE": "{", "RBRACE": "}"}


def lexer(contents):
    lines = contents.split("\n")
    char_to_token = {value: key for key, value in tokens.items()}
    brace_count = 0
    in_braces = False

    for line in lines:
        chars = list(line)

        token_seq = []
        for char in chars:
            if char in char_to_token:
                token_seq.append((char_to_token[char], char))


def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens
