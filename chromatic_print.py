def chromatic_print(raw_string, hex_code):
    hex_color = hex_code.lstrip('#')
    try:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    except ValueError:
        print("[ meta-info ]: invalid hex code. please provide a valid code like '#RRGGBB'.")
        return
    print(f"\033[38;2;{r};{g};{b}m{raw_string}\033[0m")

chromatic_print("Hello, World!", "#0")
