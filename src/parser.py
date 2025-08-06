tokens = {
    "LBRACE": "{",
    "RBRACE": "}",
    "WHITESPACE": "  ",
    "DQUOTE": '"',
    "SQUOTE": "'",
    "COLON": ":",
}


def lexer(contents):
    lines = contents.split("\n")
    char_to_token = {value: key for key, value in tokens.items()}

    temp_string = ""
    quote_count = 0
    brace_count = 0
    key_count = 0
    value_count = 0

    for line in lines:
        chars = list(line)

        token_seq = []
        for char in chars:
            if char in char_to_token:
                # Braces logic
                if char == "}" or char == "{":
                    brace_count += 1

                if brace_count % 2 == 0:
                    in_braces = False
                else:
                    in_braces = True

                # Quotes logic
                if char == "'" or char == '"':
                    quote_count += 1

                if quote_count % 2 == 0:
                    in_quotes = False

                    """
                    If closing quote has been found, string tokenization ends,
                    key / value token is assigned, depending on colon presence,
                    temporary string is cleared
                    """
                    if len(temp_string) and ("COLON", ":") in token_seq:
                        token_seq.append(("VALUE", temp_string))
                        value_count += 1
                        temp_string = ""
                    elif len(temp_string) and ("COLON", ":") not in token_seq:
                        token_seq.append(("KEY", temp_string))
                        key_count += 1
                        temp_string = ""
                else:
                    in_quotes = True

                token_seq.append((char_to_token[char], char))

            else:
                # Creating a string, because lexer found string opening quote
                if in_quotes == True:
                    temp_string += char

        print(token_seq)

    if (
        token_seq
        and brace_count >= 2
        and brace_count % 2 == 0
        and in_braces == False
        and in_quotes == False
        and key_count >= 1
        and value_count >= 1
        and key_count == value_count
    ):
        print("correct json file")
        return 0
    else:
        print("wrong json file")
        return 1


def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens
