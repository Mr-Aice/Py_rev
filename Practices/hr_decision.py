from typing import Callable

acceptance: Callable[[str, str], str] = lambda name, domain : f"Congrats {name}! You have been selected for internship in the domain of {domain}.\n For more information, kindly visit portal."

rejection: Callable[[str, str], str] = lambda name, domain : f"Dear {name}! We regret to inform you that your application for internship in domain of {domain} has been rejected. \n For more information, kindly visit your portal."

fired: Callable[[str, str], str] = lambda name, domain : f"Dear {name}! We regret to inform you that you have been fired from your position of {domain}. \n For more information, kindly visit your portal."


promotion: Callable[[str, str], str] = lambda name, domain : f"Congrats {name}! You have been promoted in the domain of {domain}.\n For more information, kindly visit portal."


def get_Person_Data() -> str:
    name: str = input("Please write the name of person: ")
    domain: str = input("Domain of the person: ")
    return name, domain

def get_Decision() -> int:
    while True:
        try:
            choice:int = int(input(
                    f"""
                    Please Choose email you want to send 1-4 from the following:
                    1. Acceptance Email
                    2. Rejection Email
                    3. Fired Email 
                    4. Promotion Email
                    Your Choice: """))
            return choice
        except:
            print(f"Wrong Choice!!! Please try again.")
            continue


def toughDecision() -> Callable[[], str]:
    
    name, domain = get_Person_Data()
    choice = get_Decision()
    
    match choice:
            case 1:
                return acceptance(name, domain)
            case 2:
                return rejection(name, domain)
            case 3:
                return fired(name, domain)
            case 4:
                return promotion(name, domain)
            case _:
                return f"Wrong Input!!! Please try again!"
    


def main():
    while True:
        print(
            f"""
        Dear HR!
        We hope you are ready to make your decision. Please make sure that you are ready to own the responsibility of what you are going to do.
        """
        )

        decision: str = "y yes n No".lower()
        ans: str = input("Please type Y to proceed or N to exit: ").lower()

        if (ans in decision):
            print("Hi!")
            if (ans == "y" or ans == "yes"):
                print(toughDecision())
                break
            else:
                print("Take your time and come back when you are ready to make your decision!")
                break
    return


main()
    










    
    
            
            

