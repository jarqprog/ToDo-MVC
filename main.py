from controller import Controller


def main():
    Controller.view.display_intro()
    user = Controller()
    user.menu_loop()


if __name__ == "__main__":
    main()
