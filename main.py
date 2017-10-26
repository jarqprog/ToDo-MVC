from controller import Controller


def main():
    Controller.view.display_intro()
    controller = Controller()
    controller.menu_loop()


if __name__ == "__main__":
    main()
