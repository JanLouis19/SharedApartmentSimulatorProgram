# SharedApartmentSimulatorProgram
A simulator about the daily living in an shared apartment with 11 people.

Content:   1: Explanation,    2: How to run,   3: important to know


1: Explanation:
The main functionality of the program is the random simulator of the 11 co-residents's decisions. They can either leave/enter the house or enter/leave one of the three bathrooms in the house. As the rooms of the residents are located in different places of the 2 floor-apartment, they have individual preferences to which bathroom they before, as the bathrooms are located in different places in the house (one on top floor and 2 on the lower floor). When the simulator is started, every resident starts as a own thread. Every 2 seconds, every resident gets a random number, which decides the action that he wants to do right now (leave house, enter house, leave bathroom 1 etc...). After the action that is wanted in this 'round' has been decided, the programm checks 
