from safeopen import open_file, write_file

def main():
    content = open_file("pan_tadzio.txt")
    print(content)

    text_to_save = "lalalal\n123"
    write_file('text.txt', text_to_save)

if __name__ == "__main__":
    main()