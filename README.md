## Help MacGyver get out the labyrinth

This application is a Labyrinth game in which you play MacGyver and have to escape by killing the guard with a homemade syringe with way too much ether in it.

### Installation:

- To install and run this app, clone the repository by running:
```
git clone https://github.com/adrien914/P3_Aidez_MacGyver_a_s-echapper-.git
```
    
- Install virtualenv if it's not already done:
```
pip3 install virtualenv
```
- Create a virtual environment by running:
```
virtualenv venv
```
- Activate the virtual environment by running:
```
source venv/bin/activate
```
- If you're not already there move to the root of the application:
```bash
cd P3_01_programme
``` 
- Install the requirements by running:
```
pip3 install -r requirements.txt
```
- Run the program by running:
```
python3 Main.py
```
- This program works with Linux, Windows and MacOS

#### Map limits:

- The map has to be at most 15 tiles wide and 15 tiles tall

- The map is in a file named sample_map.txt in the directory maps at 
the root of the application

#### Map notation:
        
- x for a wall
- blank space for a crossable tile
- P for player's starting position
- E for the enemy
- G for the goal
   
#### Controls:

- Use the arrow keys to move
- Walk on items to retrieve them

#### Goal:

- Your goal is to get to the exit of the labyrinth.
     
- To achieve this goal you have to get the three items scattered on the 
map to craft a syringe and make the guardian disappear
