import pandas as pd
import numpy as np
import random

# RESOURCE: https://github.com/Ryota-Kawamura/Mathematics-for-Machine-Learning-and-Data-Science-Specialization/blob/main/Course-3/Week-2/C3_W2_Lab_2_Dice_Simulations.ipynb

class Die:
    """
    A class representing a Die (2-Face: Die of type Coin or 6-Face Die )

    Attributes:
       
        _privateDataFrame (pd.DataFrame): Used to hold both die face and weight data points
    
    Methods:
        __init__():
        change_die_weight() 
        roll_die()
        die_state()
    """

    # Class attributes None

    # Instance attributes
    def __init__(self, theDie: np.array) -> None:
       
        """Initializes Die Class
           Initializes the weights to 1 for each die face
           Saves die faces and weights _privateDataFrame with die faces in the index

        Args:
            theDie (np.array):  NumPy array of Die faces where array dtype(strings|numbers)

        Raises:
            ValueError: If die faces are not distinct values
            TypeError: If die is not of type NumPy Array 

        Returns:
            None
        """

        print(f"The Inital Type: {type(theDie)}")

        #Must be NumPy Array
        if not type(theDie) is np.ndarray:
            raise TypeError("The die must be of type NumPy Array!") 
        #The Die Must have 2(Coin) or 6(Die) Distinct values
        #print(f"Number of Die Faces: {len(np.unique(theDie))}")
        #print(f"Not Equal 6? {len(np.unique(theDie)) != 6}")
        if ( len(np.unique(theDie)) != 2 ) and ( len(np.unique(theDie)) != 6):
            raise ValueError(f"The die must have 2(Coin) or 6(Die) distinct values! {theDie}")
        
        #Build Dynamic Index
        self.theDie = theDie
        #self.privateDataFrame: pd.DataFrame = pd.DataFrame(self.theDie, columns=['dieValue'], index=['Face1', 'Face2', 'Face3', 'Face4', 'Face5', 'Face6'] )
        self._privateDataFrame: pd.DataFrame = pd.DataFrame(self.theDie, columns=['dieValue'], index=[ 'Face' + str(n) for n in range(1,len(np.unique(theDie)) + 1) ] )

        #startFace: str = [ 'Face' + str(n) for n in range(1,len(np.unique(theDie)) + 1) ][0]
        #endFace: str = [ 'Face' + str(n) for n in range(1,len(np.unique(theDie)) + 1) ][-1]
        #Initialize die weights to 1.0
        #self.privateDataFrame.loc['Face1':'Face6'] = 1.0
        #self.privateDataFrame.loc["'" + startFace + "'":"'" + endFace + "'"] = 1.0

        for idx, row in self._privateDataFrame.iterrows():
            #Modify Face Value
            self._privateDataFrame.loc[idx] = 1.0
            #print(f"Index: {idx2}")
            #print(f"Weight for {idx2}: {row2['dieValue']}")

    # Instance method change_die_weight
    def change_die_weight(self, face_name: str, new_weight: float) -> None:
        """
        Takes two arguments: face_name  new_weight
        Checks:  
            face_name: must exist in die array (If not, raises an IndexError)
            new_weight: must be of type float and castable as numeric (If not, raises a TypeError)

        Actions:
            If new weight is of type float, subtract 1 from new weight to obtain the percentage which will be distributed among the 
            remaining die faces

            If new weight is of type int, convert integer to float  then subtract 1 from generated float to obtain the percentage which will be distributed among the 
            remaining die faces

        Note(s):  Weights must sum to 1
        """

        #Get the length of the dataFrame
        dataFrameLength: int = len(self._privateDataFrame)
        
        #face_name must Exist in the die array
        if not (face_name in self._privateDataFrame.index):
             raise IndexError(f"{face_name} does not exist in the die array: ")
        print(f"New Weight Type: {type(new_weight)}" )
        #new_weight must be numeric or castable as numeric
        if not isinstance(new_weight, (int, float)):  
            raise TypeError(f"new weight request must be of type integer or float: {new_weight}")
        
        if isinstance(new_weight, (float)):
            #Set all die faces
            for idx, row in self._privateDataFrame.iterrows():
                #Modify Face Value
                self._privateDataFrame.loc[idx] = (1 - new_weight)/(dataFrameLength - 1)

            #self.privateDataFrame.loc['Face1':'Face6'] = (1 - new_weight)/5
            #self.privateDataFrame.loc['Face1':'Face6'] = (1 - new_weight)/dataFrameLength - 1
            #self.privateDataFrame.loc["'" + startFace + "'":"'" + endFace + "'"] = (1 - new_weight)/dataFrameLength - 1
        
            #Modify the requested die face
            #self.privateDataFrame.loc[face_name] = new_weight

        if isinstance(new_weight, (int)):
            #Convert integer to float
            new_weight = float(new_weight)

            #Set all die faces
            print(f"Potential Data Frame Row Values: {(1 - new_weight)/(dataFrameLength - 1)}" )
            for idx, row in self._privateDataFrame.iterrows():
                #Modify Face Value
                self._privateDataFrame.loc[idx] = (1 - new_weight)/(dataFrameLength - 1)
            #self.privateDataFrame.loc['Face1':'Face6'] = (1 - new_weight)/5
            #self.privateDataFrame.loc['Face1':'Face6'] = (1 - new_weight)/dataFrameLength - 1
            #self.privateDataFrame.loc["'" + startFace + "'":"'" + endFace + "'"] = (1 - new_weight)/dataFrameLength - 1

        
        #Modify the requested die face
        self._privateDataFrame.loc[face_name] = new_weight
    
    # Instance method roll_die
    def roll_die(self, how_many_times: int = 1) -> list:
        """
        Simulates a dice roll with weighted probabilities for each face.
        
        Arg Checks:  
            how_many_times: number of requested die rolls; default is 1 roll

        Returns:
            a python list of outcomes
        """

        print(f"Entering roll_die: {how_many_times}")
       
        
        #Die roll outcome list set to zero list entries
        outcomes: list = list()

        #Make sure the die is properly weighted!
        for idx, tblRow in self._privateDataFrame.iterrows():
            print(f"Index: {idx}")
            print(f"Weight for {idx}: {tblRow['dieValue']}")
            print("-" * 20)

        facesList: list = self._privateDataFrame.index.to_list()
        weightsList: list = self._privateDataFrame['dieValue'].to_list()

        for roll in range(how_many_times):
            
            print(f"Roll Number: {roll + 1}")

            if ( (roll+1) == how_many_times):
                #Show the selected die face
                #Set all die faces to 0.0
                self._privateDataFrame.loc[facesList[0]:facesList[-1]] = 0.0
                #Set the randomly selected die face of the die that we have a hit on
                #Append the result to the outcomes list
                outcomes.append(random.choices(facesList, weights=weightsList, k=1)[0])
                self._privateDataFrame.loc[outcomes[-1], 'dieValue'] = 1.0  #This will represent die state
                
                #Now that We have a hit, use the break statement to
                #terminate this inner loop to prevent the recording of
                #another die face value
            else:
                #outcomes.append(index)
                outcomes.append(random.choices(facesList, weights=weightsList, k=1)[0])
                    
        return outcomes
    
    # Instance method die_state
    def die_state(self) -> list:
        """
        Takes no arguments
        
        Returns a copy of the private data frame
        """
        return self._privateDataFrame
    
    
if __name__ == '__main__':

    # The Die
    theDie: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)

    results: str = ""
    # Instantiate the Die class
    myInstance: Die = Die(theDie)
    print("Type Check:\n", type(myInstance))
    print(f"Show list of attribute for object: {dir(myInstance)} \n")
    print(f"Is instance an object of class Die: {isinstance(myInstance, Die)} \n")
    
    #print(f"TTTTT: {myInstance._privateDataFrame}")
    #print(f"TTTTT: {myInstance.die_state}")

    myInstance.change_die_weight('Face3', .30)

    print(f"Outcomes: \n{myInstance.roll_die(3)}")

    dieStateDataFrame: pd.DataFrame = myInstance.die_state()
    print(f"Die State: {dieStateDataFrame}")


    # The Coin
    theCoin: np.array = np.array([1.0, 2.0], dtype=float)

    results: str = ""
    # Instantiate the Die class
    myCoinInstance: Die = Die(theCoin)
    
    myCoinInstance.change_die_weight('Face2', .30)

    print(myCoinInstance.roll_die(1))

    dieStateDataFrame: pd.DataFrame = myCoinInstance.die_state()
    print(f"Die State: {dieStateDataFrame}")
    #results = myInstance.add_book("War of the worlds", 4)
    #print(results)
    #results = myInstance.add_book("Embrace the Challenge", 5)
    #myInstance.has_read("Embrace the Challenge")
    #print(results)
    #results = myInstance.add_book("Embrace the Challenge", 5)
    
    #print(results)
    #print(f"Reader's favorite books: {myInstance.fav_books()}")

    #newDataFrame: pd.DataFrame = myInstance.fav_books()
    #all3s: bool = (newDataFrame['book_rating'] > 3).all()
    #print(newDataFrame[newDataFrame['book_rating'] < 3])
    #print(f"Do all books in the list have a rating > 3? Response: {all3s}")


    # Access instance attributes
    #print(myInstance.num_books)

    # Call instance method num_books_read
    #print(myInstance.num_books_read())

    #num_args = 3
    #assert num_args == 3, "number of arguments must be 3!"
    