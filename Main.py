# Main.py
from box_office import Box_office

class BoxOfficeAnalyzer:
    def __init__(self, box_office_data):
        self.box_office_data = box_office_data

    def report_box_office_earnings(self, film_id):
        try:
            film_entries = self.box_office_data.read_items(film_id=film_id)
            total_earnings = sum(entry['earnings'] for entry in film_entries)
            average_earnings = total_earnings / len(film_entries)
            max_earning_items = max(film_entries, key=lambda x: x['earnings'])
            print("Report for Film ID:", film_id)
            print("Total Earnings:", total_earnings)
            print("Average Earnings per Theater:", average_earnings)
            print("Theater with Highest Earnings:", max_earning_items['theater_id'])
        except Exception as e:
            print("Error:", e)

    def compare_earnings_across_theaters(self, comparison_data):
        earnings_comparison = {}
        for theater_id in comparison_data:
            try:
                theater_entries = self.box_office_data.read_items(theater_id=theater_id)
                total_earnings = sum(entry['earnings'] for entry in theater_entries)
                earnings_comparison[theater_id] = total_earnings
            except Exception as e:
                print("Error while comparing theater", theater_id, ":", e)
        print("Comparison of Earnings Across Theaters:", earnings_comparison)

    def create_item(self, film_id, theater_id, earnings):
        try:
            self.box_office_data.create_items(film_id, theater_id, earnings)
            print("Item created successfully.")
            self.show_box_office()
        except Exception as e:
            print("Error:", e)

    def update_item(self, film_id, theater_id, new_earnings):
        try:
            # Convert new_earnings to float
            new_earnings = float(new_earnings)
            self.box_office_data.update_items(film_id, theater_id, new_earnings)
            print("Item updated successfully.")
            self.show_box_office()
        except Exception as e:
            print("Error:", e)

    def delete_item(self, film_id, theater_id):
        try:
            self.box_office_data.delete_items(film_id, theater_id)
            print("Item deleted successfully.")
            self.show_box_office()
        except Exception as e:
            print("Error:", e)

    def show_box_office(self):
        all_entries = self.box_office_data.read_items()
        print("\nThe current data of box-office is:\n")
        for entry in all_entries:
            print("Film ID:", entry['film_id'])
            print("Theater ID:", entry['theater_id'])
            print("Earnings:", entry['earnings'])
            print()

if __name__ == "__main__":
    box_office = Box_office()
    box_office.create_items('film1', 'theater1', 1000)
    box_office.create_items('film2', 'theater1', 1500)
    box_office.create_items('film1', 'theater1', 1000)
    box_office.create_items('film2', 'theater1', 1500)
    box_office.create_items('film3', 'theater1', 1200)
    box_office.create_items('film4', 'theater1', 2550)
    box_office.create_items('film5', 'theater1', 1800)
    box_office.create_items('film1', 'theater2', 2500)
    box_office.create_items('film2', 'theater2', 1800)
    box_office.create_items('film3', 'theater2', 1800)
    box_office.create_items('film4', 'theater2', 1880)
    box_office.create_items('film5', 'theater2', 1800)
    box_office.create_items('film1', 'theater3', 1500)
    box_office.create_items('film2', 'theater3', 1800)
    box_office.create_items('film3', 'theater3', 1800)
    box_office.create_items('film4', 'theater3', 1600)
    box_office.create_items('film5', 'theater3', 1807)
    box_office.create_items('film1', 'theater4', 2200)
    box_office.create_items('film2', 'theater4', 1800)
    box_office.create_items('film3', 'theater4', 1800)
    box_office.create_items('film4', 'theater4', 1850)
    box_office.create_items('film5', 'theater4', 1800)
    box_office.create_items('film1', 'theater5', 2800)
    box_office.create_items('film2', 'theater5', 1700)
    box_office.create_items('film3', 'theater5', 2800)
    box_office.create_items('film4', 'theater5', 2800)
    box_office.create_items('film5', 'theater5', 3500)

    print("Welcome to Box Office Report!")
    analyzer = BoxOfficeAnalyzer(box_office)
    while True:
        print("\nHow may I help you?")
        help_input =int(input("Enter your request ('analysis(1)', 'create(2)', 'update(3)', 'delete(4)', 'exit(5)'): "))

        if help_input == 1:
            print("What analysis would you like to perform?")
            analysis_type = input("Enter 'film' for film earnings or 'total' for total earnings: ")

            if analysis_type.lower() == "film":
                film_id = input("Enter the film ID: ")
                analyzer.report_box_office_earnings(film_id)
            elif analysis_type.lower() == "total":
                analyzer.compare_earnings_across_theaters(['theater1', 'theater2', 'theater3', 'theater4', 'theater5'])
            else:
                print("Sorry, we don't have information about that.")

        elif help_input == 2:
            film_id = input("Enter the film ID: ")
            theater_id = input("Enter the theater ID: ")
            earnings = float(input("Enter the earnings: "))
            analyzer.create_item(film_id, theater_id, earnings)

        elif help_input == 3:
            film_id = input("Enter the film ID: ")
            theater_id = input("Enter the theater ID: ")
            new_earnings = input("Enter the new earnings: ")
            analyzer.update_item(film_id, theater_id, new_earnings)

        elif help_input== 4:
            film_id = input("Enter the film ID: ")
            theater_id = input("Enter the theater ID: ")
            try:
                analyzer.delete_item(film_id, theater_id)
            except Exception as e:
                print("Data not found.")

        elif help_input ==5:
            print("Exiting...")
            breakpython 