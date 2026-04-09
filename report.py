from colorama import Fore, Style

def generate_report(results):
    print("\nhere is the result... eh!!!\n")

    if not results:
        print(Fore.GREEN + "The url is loyal to the family boss!\n")
        return

    for res in results:
        print(Fore.RED + f"aye Boss he gave the word in {res['type']} your pal {res['url']} can't be trusted!!!")
        print(Fore.YELLOW + f"    Payload: {res['payload']}\n")
