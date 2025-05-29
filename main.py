"""
Hello World! Desiree Cele created a Buffalo-Cheektowaga Housing Data Explorer: 
This program analyzes and displays a real-world housing statistics sample from S2501 OCCUPANCY CHARACTERISTICS Buffalo-Cheektowaga, NY metro area. 
It allows users to extract key data points(raw data), exploring occupancy rates, household sizes, and housing types with margin-of-error data. 
The tool reads from a CSV dataset, analyses housing records in seconds and provides an interactive menu for simple data exploration.
"""

import csv

def load_housing_data(filename):
    """Load housing data from text file (CSV format)."""
    data = []
    try:
        with open(filename, mode='r') as file:
            # Read the first line as headers
            headers = file.readline().strip().split(',')
            for line in file:
                values = line.strip().split(',')
                if len(values) == len(headers):
                    data.append(dict(zip(headers, values)))
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def display_categories(data):
    """Display available data categories."""
    categories = set()
    for row in data:
        categories.add(row['Category'])
    print("\nAvailable Categories:")
    for i, category in enumerate(sorted(categories), 1):
        print(f"{i}. {category}")
    return sorted(categories)

def display_subcategories(data, category):
    """Display subcategories for a selected category."""
    subcategories = []
    for row in data:
        if row['Category'] == category:
            subcategories.append(row['Subcategory'])
    
    if not subcategories:
        print("No subcategories found for this category.")
        return None
    
    print(f"\nSubcategories for '{category}':")
    for i, subcat in enumerate(subcategories, 1):
        print(f"{i}. {subcat}")
    return subcategories

def display_housing_stats(data, category, subcategory):
    """Display statistics for a specific category and subcategory."""
    for row in data:
        if row['Category'] == category and row['Subcategory'] == subcategory:
            print(f"\nHousing Statistics for {category} - {subcategory}:")
            print("-" * 50)
            print(f"Occupied housing units (Estimate): {row['Occupied_Estimate']}")
            print(f"Occupied housing units (Margin of Error): ±{row['Occupied_Margin']}")
            print(f"Percent occupied (Estimate): {row['Occupied_Percent_Estimate']}%")
            print(f"Percent occupied (Margin of Error): ±{row['Occupied_Percent_Margin']}%")
            print(f"Owner-occupied units (Estimate): {row['Owner_Estimate']}")
            print(f"Owner-occupied units (Margin of Error): ±{row['Owner_Margin']}")
            print(f"Percent owner-occupied (Estimate): {row['Owner_Percent_Estimate']}%")
            print(f"Percent owner-occupied (Margin of Error): ±{row['Owner_Percent_Margin']}%")
            print(f"Renter-occupied units (Estimate): {row['Renter_Estimate']}")
            print(f"Renter-occupied units (Margin of Error): ±{row['Renter_Margin']}")
            print(f"Percent renter-occupied (Estimate): {row['Renter_Percent_Estimate']}%")
            print(f"Percent renter-occupied (Margin of Error): ±{row['Renter_Percent_Margin']}%")
            return
    print(f"No data found for {category} - {subcategory}")

def main():
    print("Buffalo-Cheektowaga, NY Metro Area Housing Data Explorer")
    print("=" * 60)
    
    # Load data
    data = load_housing_data('Housing_data.txt')
    if not data:
        return
    
    while True:
        print("\nMain Menu:")
        print("1. Explore housing data by category")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ").strip()
        
        if choice == '1':
            # Display categories
            categories = display_categories(data)
            if not categories:
                continue
                
            # Get category selection
            try:
                cat_choice = int(input("\nEnter category number (or 0 to go back): "))
                if cat_choice == 0:
                    continue
                if cat_choice < 1 or cat_choice > len(categories):
                    print("Invalid selection. Please try again.")
                    continue
                
                selected_category = categories[cat_choice - 1]
                
                # Display subcategories
                subcategories = display_subcategories(data, selected_category)
                if not subcategories:
                    continue
                    
                # Get subcategory selection
                try:
                    subcat_choice = int(input("\nEnter subcategory number (or 0 to go back): "))
                    if subcat_choice == 0:
                        continue
                    if subcat_choice < 1 or subcat_choice > len(subcategories):
                        print("Invalid selection. Please try again.")
                        continue
                    
                    selected_subcategory = subcategories[subcat_choice - 1]
                    
                    # Display statistics
                    display_housing_stats(data, selected_category, selected_subcategory)
                    
                    input("\nPress Enter to continue...")
                    
                except ValueError:
                    print("Please enter a valid number.")
                    
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '2':
            print("Exiting the Housing Data Explorer. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()