- [ ] Film Polling
    ###### If anyone wants help with a film suggestion
- [ ] Film object
    - [X] Film time set/get
    - [X] Film date set/get
    - [X] Magnet set/get
    - [ ] Movie details
        - [ ] trailer
        - [ ] imdb/rotten tomatoes/wiki
    - [ ] Film info, returns all information added to film object
- [ ] Film tickets
    ###### So we know who wants to attend a film
    - [X] by adding a reaction to a film post
    - [X] by using a 'purchase ticket command'
    - [ ] Refund ticket function: WIP, currently errors loading an empty list back into json
- [ ] Reminder
    - [ ] Tag ticket owners in in channel 1 day/ 1 hour before film
    - [ ] Direct message ticket owners
- [ ] Multiple film support, unique jsons
    - [ ] Auto deletes film a day after the event
- [ ] Google Sheets integration
- [ ] Calendar integration
    ###### Create a calendar object that people can use to create an event in whicever service they want 
- [ ] Pause/Play countdown timer, for non syncplay users
- [ ] Bot init/config, asks which roles to mention in messages
- [X] Migrate to discord.py v1.3
- [ ] Refactor commands
    - [X] Move info getter & info setter into BaseCommand
    - [X] Move save_dict_location into BaseCommand
    - [ ] Change to using dictionary, as there errors in the dic <> json interface
        - [ ] Use pickle, or alternative as a store
- [ ] Allow for multiple channels to use the bot
- [ ] Refactor: move parameter & arg check to commands as the command should dictate
it's own rules for it's parameter requirements
