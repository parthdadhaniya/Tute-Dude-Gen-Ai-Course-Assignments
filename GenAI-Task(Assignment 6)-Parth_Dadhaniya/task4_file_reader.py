# Task 4: Safe File Reader Utility
# Reading first 3 lines of a file with exception handling and finally cleanup

def read_first_three_lines():
    print("--- Safe File Reader ---")
    filename = input("Enter file path to read (e.g. sample.txt): ").strip()

    file_obj = None
    try:
        file_obj = open(filename, 'r')
        print(f"\n--- First 3 lines of '{filename}' ---")
        
        # Requirement: Print ONLY the first 3 lines of the file
        for i in range(3):
            line = file_obj.readline()
            if not line:
                break
            print(line, end="")
        print()

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")

    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    else:
        print("[Success]: File read successfully.")

    finally:
        # Close file if it was successfully opened
        if file_obj is not None:
            file_obj.close()
            print("[Cleanup]: File stream closed successfully.")

if __name__ == "__main__":
    read_first_three_lines()
