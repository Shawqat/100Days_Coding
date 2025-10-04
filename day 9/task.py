# a program that analyzes two lists of data using set operations
def data_analyzer():
    # Sample data - website visitors on two different days
    day1_visitors = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
    day2_visitors = ["Charlie", "Diana", "Eve", "Henry", "Ivan", "Julia", "Alice"]
    
    # Convert to sets for analysis
    set_day1 = set(day1_visitors)
    set_day2 = set(day2_visitors)
    
    while True:
        print("\n=== WEBSITE VISITOR ANALYSIS ===")
        print("1. Show all unique visitors")
        print("2. Show returning visitors")
        print("3. Show new visitors (day 2 only)")
        print("4. Show visitors who only came once")
        print("5. Compare with custom visitor list")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            all_visitors = set_day1 | set_day2
            print(f"\nAll unique visitors ({len(all_visitors)} total):")
            print(sorted(all_visitors))
            
        elif choice == "2":
            returning = set_day1 & set_day2
            print(f"\nReturning visitors ({len(returning)} people):")
            print(sorted(returning))
            
        elif choice == "3":
            new_day2 = set_day2 - set_day1
            print(f"\nNew visitors on day 2 ({len(new_day2)} people):")
            print(sorted(new_day2))
            
        elif choice == "4":
            only_once = set_day1 ^ set_day2
            print(f"\nVisitors who only came once ({len(only_once)} people):")
            print(sorted(only_once))
            
        elif choice == "5":
            custom_input = input("Enter visitor names separated by commas: ")
            custom_list = [name.strip() for name in custom_input.split(",")]
            custom_set = set(custom_list)
            
            print(f"\nAnalysis with your custom list:")
            print(f"Common with day 1: {custom_set & set_day1}")
            print(f"Common with day 2: {custom_set & set_day2}")
            print(f"Not seen either day: {custom_set - (set_day1 | set_day2)}")
            
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

# Run the main program
data_analyzer()