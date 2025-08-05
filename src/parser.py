import re

tokens = {
    "LBRACE": "{",
    "RBRACE": "}",
    "WHITESPACE": " ",
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
                    # If closing quote has been found, string tokenization ends and
                    # temporary string is cleared
                    if len(temp_string):
                        token_seq.append(("STRING", temp_string))
                        temp_string = ""
                else:
                    in_quotes = True

                token_seq.append((char_to_token[char], char))

            else:
                # Creating a string, because lexer found starting quote
                if in_quotes == True:
                    temp_string += char

        print(token_seq)

    if token_seq and brace_count >= 2 and brace_count % 2 == 0 and in_braces == False:
        print("correct json file")
        return 0
    else:
        print("wrong json file")
        return 1


def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens
