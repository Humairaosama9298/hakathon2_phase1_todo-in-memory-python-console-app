"""
Todo In-Memory Python Console App
Entry point for the application
"""

from todo_app.cli.menu import Menu


def main():
    """Main function to run the todo application"""
    # Create and run the menu system
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()