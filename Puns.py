import requests
def get_random_joke() :
    url = "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw&type=twopart"
    response = requests.get(url)
    if response.status_code == 200 :
        joke = response.json()
        return f" {joke['setup']}\n {joke['delivery']}\n"
    else :
        return 'Error! The puns are offline.'
def main() :
    print('\n------ ⚡PUN - BELIEVABLE⚡ -----\n')
    while True :
        user_input = input("Press enter to get a pun or q to exit : ").strip().lower()
        print("\n")
        if user_input in ('q', 'exit') :
            print('Goodbye !\n')
            break
        joke = get_random_joke()
        print(joke)
if __name__ == "__main__" :
    main()