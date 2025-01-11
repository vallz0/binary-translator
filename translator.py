class BinaryTranslator:
    @staticmethod
    def encode_to_binary(text: str) -> str:
        return ' '.join(format(ord(char), '08b') for char in text)

    @staticmethod
    def decode_from_binary(binary: str) -> str:
        try:
            return ''.join(chr(int(b, 2)) for b in binary.split())
        except ValueError:
            raise ValueError("Invalid input: ensure the binary is correct and space-separated.")


class TranslatorApp:
    def __init__(self) -> None:
        self.translator = BinaryTranslator()

    def show_menu(self) -> None:
        print("-" * 50)
        print("Binary Translator".center(50))
        print("-" * 50)
        print("\n[1] Encode")
        print("[2] Decode")
        print("[3] Exit")

    def handle_choice(self, choice: int) -> None:
        match choice:
            case 1:
                self.handle_encoding()
            case 2:
                self.handle_decoding()
            case 3:
                print("\nExiting the program. Goodbye!")
            case _:
                print("Invalid option. Try again.")

    def handle_encoding(self) -> None:
        text = input("Enter the text to encode: ")
        binary = self.translator.encode_to_binary(text)
        print("\nEncoded text in binary:")
        print(binary)

    def handle_decoding(self) -> None:
        binary = input("Enter the binary to decode: ")
        try:
            text = self.translator.decode_from_binary(binary)
            print("\nDecoded text:")
            print(text)
        except ValueError as e:
            print(f"Error: {e}")

    def run(self) -> None:
        while True:
            self.show_menu()
            try:
                choice = int(input("What would you like to do? "))
                if choice == 3:
                    self.handle_choice(choice)
                    break
                self.handle_choice(choice)
            except ValueError:
                print("Error: Please enter a valid number.")
