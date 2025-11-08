# Vars
infAccount = {'name': '', 'numbers': 0, 'type': ''}

# Functions
def main():
    while True:
        try:
            infAccount['name'] = input("Put a name: ")
            infAccount['numbers'] = int(input("Number of account: "))
            AccountMoney = 0
            AccountStatus = False
            print()

            while True:
                print("[0] Account Status\n"
                      "[1] Open account\n"
                      "[2] Close account\n"
                      "[3] Withdraw\n"
                      "[4] Deposite\n"
                      "[5] Finish service\n")
                opc = int(input("Choice one of the options above: "))
                print()


                # Commands
                if opc == 1:
                    if AccountStatus is True:
                        print("This account already exists.")
                    else:
                        infAccount['type'] = input("Type of account (CC or CPP): ").strip().lower()

                        if infAccount['type'] == "cc":
                            AccountMoney = 19
                        elif infAccount['type'] == "cpp":
                            AccountMoney = 28
                        else:
                            print("ERROR: Invalid option.")
                            continue
                        AccountStatus = True
                        print("Account created with successfully!")


                elif opc == 0:
                    print("=== ACCOUNT STATUS ===")
                    print(f"Username: {infAccount['name']}\n"
                          f"Number of account: {infAccount['numbers']}\n"
                          f"Tip of account: {infAccount['type']}\n"
                          f"Balance U${AccountMoney:.2f}\n"
                          f"Status: {AccountStatus}\n")
                    print("=" * 25)
                    print()


                elif opc == 2:
                    if AccountStatus is False:
                        print("Error to try to close account: Account don't exist.")
                    elif AccountMoney > 0:
                        print("Error to try to close account: Account with money.")
                    elif AccountMoney < 0:
                        print("Error to try to close account: Debit balance.")
                    else:
                        print("Account is closed with successfully!\n")
                        AccountStatus = False

                        print("Finishing program...\n")
                        print("=== ACCOUNT STATUS ===")
                        print(f"Username: {infAccount['name']}\n"
                              f"Number of account: {infAccount['numbers']}\n"
                              f"Tip of account: {infAccount['type']}\n"
                              f"Balance U${AccountMoney:.2f}\n"
                              f"Status: {AccountStatus}\n")
                        print("=" * 25)
                        print()
                        break


                elif opc == 3:
                    if AccountMoney < 1:
                        print("ERROR: You doesn't have enough value to release this sake.")
                    else:
                        sake = float(input("Put how much you will sake: "))
                        if AccountMoney < sake:
                            print("ERROR: You doesn't have enough value to release this sake.")
                        else:
                            print(f"Sake of U${sake:.2f} released with successfully!")
                            AccountMoney -= sake


                elif opc == 4:
                    if AccountStatus is False:
                        print("ERROR: Account don't exists.")
                    else:
                        deposite = float(input("Put how much you will deposite: "))
                        AccountMoney += deposite
                        print(f"Value of U${deposite:.2f} deposited with successfully!")


                elif opc > 5:
                    print("ERROR: Please, put a valid option.")
                    continue


                elif opc == 5:
                    print("Finishing program...\n")
                    print("=== ACCOUNT STATUS ===")
                    print(f"Username: {infAccount['name']}\n"
                          f"Number of account: {infAccount['numbers']}\n"
                          f"Type of account: {infAccount['type']}\n"
                          f"Balance U${AccountMoney:.2f}\n"
                          f"Status: {AccountStatus}")
                    print("=" * 25)
                    print()
                    break
            break

        except (ValueError, TypeError):
            print("ERROR")
            continue
        except KeyboardInterrupt:
            print("\nFinished program.")
            break
