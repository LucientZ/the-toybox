from PIL import Image
import math

ascii_charset = [' ', '.', ':', '-', '=', '+', 'v', '*', 'W', '#', '%', '@']

def calculate_luminosity(r: int, g: int, b: int) -> int:
    return 0.299 * r + 0.587 * g + 0.114 * b

def rgb_to_ascii(r: int, g: int, b: int) -> str:
    index = math.floor(calculate_luminosity(r, g, b) * (len(ascii_charset) - 1) / 255)
    return ascii_charset[index] 

def rgb_to_ansi(r: int, g: int, b: int) -> int:
    if r == g and g == b:
        if r < 8:
            return 16
        elif r > 248:
            return 231

        return round(((r - 8) / 247) * 24) + 232

    return (
        16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)
    )


def convert_to_text(buffer: list[any], width: int, height: int, use_colors: bool = False) -> str:
    final_string = ""
    for i, (r, g, b, a) in enumerate(buffer):
        if a == 0:
            char = " "
        else:
            char = rgb_to_ascii(r, g, b)

        if use_colors:
            ansi_code = rgb_to_ansi(r, g, b)
            final_string += f"\033[38;5;{ansi_code}m"

        final_string += char


        if i % width == width - 1:
            final_string += '\n'
    return final_string


def main():
    in_file = input("Enter Input File: ")
    out_file = input("Enter Output File: ")
    use_color = input("Use color? (Y/n): ").lower() == "y"

    image = Image.open(in_file).convert("RGBA")
    width, height = image.size
    buffer: list[tuple[int, int, int]] = list(image.getdata())


    final = convert_to_text(buffer, width, height, use_color)

    if out_file != "":
        print(final, file=open(out_file, "w"))
    else:
        print(final, end="\033[0m\n")


if __name__ == "__main__":
    main()
