import tui
import process
import visual

def main():
    tui.display_title("Disneyland Reviews Analysis")
    reviews = process.read_csv('disneyland_reviews.csv')
    reviews = visual.clean_reviews(reviews)  # Clean reviews before further processing

    # No need to print the number of cleaned reviews
    print("Please enter the letter which corresponds with your desired menu choice:")

    while True:
        choice = tui.main_menu()
        if choice == 'A':
            view_data_menu(reviews)
        elif choice == 'B':
            visualize_data_menu(reviews)
        elif choice == 'X':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def view_data_menu(reviews):
    while True:
        choice = tui.view_data_menu()
        if choice == 'A':
            park = tui.get_input("Enter the park name: ")
            process.view_reviews_by_park(reviews, park)
        elif choice == 'B':
            park = tui.get_input("Enter the park name: ")
            location = tui.get_input("Enter the reviewer location: ")
            process.num_reviews_by_park_and_location(reviews, park, location)
        elif choice == 'C':
            park = tui.get_input("Enter the park name: ")
            year = tui.get_input("Enter the year: ")
            process.avg_score_by_year(reviews, park, year)
        elif choice == 'D':
            process.avg_score_by_park_and_location(reviews)
        elif choice == 'X':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def visualize_data_menu(reviews):
    while True:
        choice = tui.visualize_data_menu()
        if choice == 'A':
            visual.plot_reviews_per_park(reviews)
        elif choice == 'B':
            visual.plot_avg_scores_per_park(reviews)
        elif choice == 'C':
            park = tui.get_input("Enter the park name: ")
            visual.plot_top_10_locations(reviews, park)
        elif choice == 'D':
            park = tui.get_input("Enter the park name: ")
            visual.plot_monthly_avg_ratings(reviews, park)
        elif choice == 'X':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()





