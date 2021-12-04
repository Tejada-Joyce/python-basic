def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"Original List: {fruit_list}")

        # Add code to reverse and print fruit_list.
        fruit_list.reverse()
        print(f"Reversed List: {fruit_list}")

        # Add code to append "orange" to the end of fruit_list and print the list.
        fruit_list.append("orange")
        print(f"Appending 'orange' to the list: {fruit_list}")

        # Add code to find where "apple" is located in fruit_list and insert 
        # "cherry" before "apple" in the list and print the list.
        apple_index = fruit_list.index("apple")
        fruit_list.insert(apple_index, "cherry")
        print(f"Inserting 'cherry' to the list: {fruit_list}")

        # Add code to remove "banana" from fruit_list and print the list.
        fruit_list.remove("banana")
        print(f"Removing 'banana' from the list: {fruit_list}")

        # Add code to pop the last element from fruit_list and print the popped 
        # element and the list.
        last_element = fruit_list.pop()
        print(f"Popping the last element({last_element}) from the list: {fruit_list}")
        
        # Add code to sort and print fruit_list.
        fruit_list.sort()
        print(f"Sorted List: {fruit_list}")

        # Add code to clear and print fruit_list.
        fruit_list.clear()
        print(f"Cleared List: {fruit_list}")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

# At the bottom of your program write a call to the main function.
if __name__ == "__main__":
    main()