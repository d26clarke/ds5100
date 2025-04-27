import pandas as pd

import numpy as np

import sys
sys.path.append("/Users/ddclarke/development/python/uvaMSDS/DS5100/finalProject")

from chanceRollers.theDie.die import Die
from chanceRollers.game import Game

class Analyzer:
    """
    A class that provides descriptive statistical properties about a game object


    Attributes:
       
        None
    
    Methods:
        jackpots() 
        dieFaceCounter()
        dieComboCounter()
        diePermutationCounter()
    """

    def __init__(self, theGame: Game) -> None:
        """Initializes Analyzer Class with a Game object, as a single paramter

            self.theGame = theGame

        Args:
            theGame (Game):  Game object with game results

        Raises:
            ValueError: If the parameter is not a Game object

        Returns:
            None
        """
        
        print(f"The Inital Type: {type(theGame)}")

        #Must be type Game
        if not type(theGame) is Game:
            raise ValueError("The parameter must be of type Game!") 
        
        self.theGame = theGame

        print(f"Game Results (WideFormat): \n{self.theGame.playResults()}")
        print(f"Game Results (NarrowFormat): \n{self.theGame.playResults("n")}")


    
    def jackpots(self) -> int:
        
        """Computes how many times the game resulted in a jackpot 

            A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die



        Args:
            None

        Raises:
            None

        Returns:
            None
        """

        print(f"Entering method jackpots... \n")

        numberOfJackpots: int = 0

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")
        print(f"The DataFrame to examine for jackpot notifications: \n{diePlayResultsFrame}")

        #Check all rows in this dataframe
        rowsInDataFrame: int = len(diePlayResultsFrame)
        print(f"Number of Rows in DataFrame: {rowsInDataFrame}")
        #Use the following for Loop to get to each Series 
        for rowIdx in range(1,rowsInDataFrame + 1):
            print(f"Row Index: {rowIdx}")
            #Use the series duplicated function to determine if there is a jackpot
            #If the number of duplicates plus one matches the len of the series then 
            #we have a jackpot.  NOTE:  We have to add one to the number of duplicates since the first element 
            #in the series is not seen as a duplicate.
            print(f"**********************")
            print(f"DATA: \n{type(diePlayResultsFrame.loc[rowIdx])}")
            print(f"Length of the Series: {len(diePlayResultsFrame.loc[rowIdx])}")
            print(f"**********************")

            duplicates: pd.Series = diePlayResultsFrame.loc[rowIdx].duplicated()
            print(f"The Duplicates \n{duplicates}")
            num_duplicates: np.int64 = duplicates.sum()
            print(f"The Number of Duplicates \n{num_duplicates}")
            print(f"Corrected Offset: {num_duplicates + 1}")

            if len(diePlayResultsFrame.loc[rowIdx]) == num_duplicates + 1:
                #We have a jackpot
                numberOfJackpots += 1
        
        return numberOfJackpots

    def dieFaceCounter(self) -> pd.DataFrame:
        
        """Computes how many times a given face is rolled in each event.
           
            For Example:
            If a roll of five dice has all sixes, 
            then the counts for this roll would be 5 for the face value 6 and 0 for the other faces


        Args:
            None

        Raises:
            None

        Returns:
            pd.DataFrame of results
        """

        print(f"Entering dieFaceCounter...")

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")

        #print(f"Number of rolls): {len(diePlayResultsFrame)}")
        #print(f"Type: {type(diePlayResultsFrame)}")

        checkForFace1: str = 'Face1'
        checkForFace2: str = 'Face2'
        checkForFace3: str = 'Face3'
        checkForFace4: str = 'Face4'
        checkForFace5: str = 'Face5'
        checkForFace6: str = 'Face6'

        #Empty DataFrame for Die Face Counts
        df_ForFaceCounts = pd.DataFrame(columns=['Face1', 'Face2', 'Face3', 'Face4', 'Face5', 'Face6'])


        #print('*' * 50)
        for index, row in diePlayResultsFrame.iterrows():

            face1Count: int = 0
            face2Count: int = 0
            face3Count: int = 0
            face4Count: int = 0
            face5Count: int = 0
            face6Count: int = 0
            #print(f"Index(Roll Number): {index}")
            #print(f"Row Data: \n{row}")

            #print(f"Type: {type(row)}")
            #print(f"Information : {type(row.info)}")
            #print(f"Length of series: {len(row)}")
            
            face1Count = row.apply(lambda x: x == checkForFace1).sum()
            face2Count = row.apply(lambda x: x == checkForFace2).sum()
            face3Count = row.apply(lambda x: x == checkForFace3).sum()
            face4Count = row.apply(lambda x: x == checkForFace4).sum()
            face5Count = row.apply(lambda x: x == checkForFace5).sum()
            face6Count = row.apply(lambda x: x == checkForFace6).sum()
            
            #print(f"Count FACE1: {face1Count}")
            #print(f"Count FACE2: {face2Count}")
            #print(f"Count FACE3: {face3Count}")
            #print(f"Count FACE4: {face4Count}")
            #print(f"Count FACE5: {face5Count}")
            #print(f"Count FACE6: {face6Count}")
            # Add a new row to df_ForFaceCounts
            df_ForFaceCounts.loc[index] = [face1Count, face2Count, face3Count, face4Count, face5Count, face6Count]
            #print('*' * 50)
        
        """
        for index, row in diePlayResultsFrame.iterrows():
                for column in diePlayResultsFrame.columns:
                    print(f"Index(Roll Number): {index}")
                    print(f"Row Data: \n{row}")
                    print(f"Column Index(DieId): {row.index[0]}")
                    print(f"Type: {type(row)}")
                    #print(f"Information : {type(row.info)}")
                    print(f"Length of series: {len(row)}")
                    print(f"Item 1**: {row[column]} -")
                    print(f"Count FACE1: {row.apply(lambda x: x == checkForFace1).sum()}")
                    print(f"Count FACE2: {row.apply(lambda x: x == checkForFace2).sum()}")
                    print(f"Count FACE3: {row.apply(lambda x: x == checkForFace3).sum()}")
                    print(f"Count FACE4: {row.apply(lambda x: x == checkForFace4).sum()}")
                    print(f"Count FACE5: {row.apply(lambda x: x == checkForFace5).sum()}")
                    print(f"Count FACE6: {row.apply(lambda x: x == checkForFace6).sum()}")
                    print(f"XXXXXXXXXXXXXXXXXXXX")        
        """

        #Set Index Name
        df_ForFaceCounts.index.name = "RollNum"
        
        #print(f"Reset: {diePlayResultsFrame.reset_index()}")
        #print(f"Face Counts DataFrame: \n{df_ForFaceCounts}")

        return df_ForFaceCounts


    def dieComboCounter(self) -> pd.DataFrame:
        
        """Computes the distinct combinations of faces rolled, along with their counts
           
            NOTE:  Combinations are order-independent and may contain repetitions
                   The data frame should have a MultiIndex of distinct combinations and a column for the associated counts


        Args:
            None

        Raises:
            None

        Returns:
            pd.DataFrame of results
        """

        print(f"Entering dieComboCounter...") 

         #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")

        """
        checkForFace1: str = 'Face1'
        checkForFace2: str = 'Face2'
        checkForFace3: str = 'Face3'
        checkForFace4: str = 'Face4'
        checkForFace5: str = 'Face5'
        checkForFace6: str = 'Face6'

        #Empty DataFrame for Die Face Counts
        df_ForFaceCounts = pd.DataFrame(columns=['Face1', 'Face2', 'Face3', 'Face4', 'Face5', 'Face6'])

        print('*' * 50)
        for index, row in diePlayResultsFrame.iterrows():

            face1Count: int = 0
            face2Count: int = 0
            face3Count: int = 0
            face4Count: int = 0
            face5Count: int = 0
            face6Count: int = 0
            #print(f"Index(Roll Number): {index}")
            #print(f"Row Data: \n{row}")

            #print(f"Type: {type(row)}")
            #print(f"Information : {type(row.info)}")
            #print(f"Length of series: {len(row)}")
            
            face1Count = row.apply(lambda x: x == checkForFace1).sum()
            face2Count = row.apply(lambda x: x == checkForFace2).sum()
            face3Count = row.apply(lambda x: x == checkForFace3).sum()
            face4Count = row.apply(lambda x: x == checkForFace4).sum()
            face5Count = row.apply(lambda x: x == checkForFace5).sum()
            face6Count = row.apply(lambda x: x == checkForFace6).sum()
            
            #print(f"Count FACE1: {face1Count}")
            #print(f"Count FACE2: {face2Count}")
            #print(f"Count FACE3: {face3Count}")
            #print(f"Count FACE4: {face4Count}")
            #print(f"Count FACE5: {face5Count}")
            #print(f"Count FACE6: {face6Count}")
            # Add a new row to df_ForFaceCounts
            df_ForFaceCounts.loc[index] = [face1Count, face2Count, face3Count, face4Count, face5Count, face6Count]
            #print('*' * 50)
        
        #Set Index Name
        df_ForFaceCounts.index.name = "RollNum"
        
        #print(f"Reset: {diePlayResultsFrame.reset_index()}")
        print(f"Face Counts DataFrame: \n{df_ForFaceCounts}")

        dfTest = df_ForFaceCounts.set_index(['Face1', 'Face2', 'Face3', 'Face4', 'Face5', 'Face6'], append=True)
        unique_combinations = dfTest.index.unique() #With Index set To RollNum and DieId
        print(f"Unique Combinations: \n{unique_combinations}")

        dfGroupByTest: pd.DataFrame = dfTest.groupby(['Face1', 'Face2', 'Face3', 'Face4', 'Face5', 'Face6']).size() 
        print(f"Group By Test: \n{dfGroupByTest}")
        """

        #print(f"Test1 \n{diePlayResultsFrame.groupby()}")
        #print(f"Column Index \n{diePlayResultsFrame.columns}")
        #print(f"Type \n{type(diePlayResultsFrame.columns)}")
        #print(f"Convert Column Index to list \n{diePlayResultsFrame.columns.to_list()}")
        #print(f"Data Frame Index \n{diePlayResultsFrame.index}")
        #Seet Multiple Index 
        dfMultiIndex = diePlayResultsFrame.set_index(diePlayResultsFrame.columns.to_list(), append=True)
        dfMultiIdxComboCnt = dfMultiIndex.groupby(diePlayResultsFrame.columns.to_list()).value_counts()
        #print(f"dfGroupByTest \n{dfMultiIdxComboCnt}")
        #print(f"dfGroupByTest Index \n{dfMultiIdxComboCnt.index}")
        #dfCombinationsTest1 = diePlayResultsFrame.set_index([1, 2, 3], append=True)
        #dfCombinationsTest1 = diePlayResultsFrame.set_index(diePlayResultsFrame.columns.to_list(), append=True)
        #unique_combinations = dfCombinationsTest1.index.unique()
        #print(f"Unique Combinations: \n{unique_combinations}")

        #dfCombsWithCounts = unique_combinations.value_counts().reset_index(name='Count')
        #dfCombsWithCounts = dfCombsWithCounts.set_index(diePlayResultsFrame.columns.to_list())
        #dfCombsWithCounts = dfCombsWithCounts.set_index(['RollNum', 1, 2, 3])
        #print(f"Unique Combinations with counts: \n{dfCombsWithCounts}")
        #print(dfCombsWithCounts.columns)

        #dfPivotTable = dfCombsWithCounts.pivot_table(index='RollNum', columns=[1, 2, 3], values='Count', aggfunc='sum')
        #dfGroupBy = dfCombsWithCounts.groupby('RollNum').size()
        #print(f"Pivot Table Combinations with counts: \n{unique_combinations}")
  
        #self.__privateGameDataFrame.pivot(index='RollNum', columns='DieId', values='DieValue')


        #dfCombinationsTest1 = diePlayResultsFrame.groupby([1, 2, 3]).first()
        #dfCombinationsTest1 = diePlayResultsFrame.groupby([1, 2, 3])
        #print(f"Test2 \n{dfCombinationsTest1}")

        #return self.theGame.playResults()
        return dfMultiIdxComboCnt
    

    def diePermutationCounter(self) -> pd.DataFrame:
        
        """Computes the distinct permutations of faces rolled, along with their counts
           
            NOTE:  Permutations are order-dependent and may contain repetitions
                   The data frame should have a MultiIndex of distinct permutations and a column for the associated counts


        Args:
            None

        Raises:
            None

        Returns:
            pd.DataFrame of results
        """

        print(f"Entering diePermutationCounter...") 

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.theGame.playResults("w")

        dfMultiIndex = diePlayResultsFrame.set_index(diePlayResultsFrame.columns.to_list(), append=True)
        dfMultiIdxPermCnt = dfMultiIndex.groupby(diePlayResultsFrame.columns.to_list()).value_counts()

        return dfMultiIdxPermCnt

       

if __name__ == '__main__':

    # The Die
    listDieOne: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
    listDieTwo: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
    listDieThree: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
    #listDieFour: np.array = np.array([1.0, 2.0], dtype=float)

    dieOneInstance: Die = Die(listDieOne)
    dieTwoInstance: Die = Die(listDieTwo)
    dieThreeInstance: Die = Die(listDieThree)
    #dieFourInstance: Die = Die(listDieFour)

    #Manage Die weighting
    dieOneInstance.change_die_weight('Face2', .20)
    dieTwoInstance.change_die_weight('Face2', .20)
    dieThreeInstance.change_die_weight('Face2', .20)


    #diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance, dieFourInstance]
    diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

    myErrorInstance: list = list(diceList)
    myInstance: Game = Game(diceList)

    #Let it roll!
    myInstance.play(10)

    myAnalyzerInstance: Analyzer = Analyzer(myInstance) 
    #myAnalyerErr: Analyzer = Analyzer(myErrorInstance)

    #Jackot Information
    print(f"Did I hit any jackpots? \n{myAnalyzerInstance.jackpots()}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.dieFaceCounter()}")

    #print(f"Play Results(Narrow Format): \n{myInstance.playResults("x")}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.dieComboCounter()}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.diePermutationCounter()}")
