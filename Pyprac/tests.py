import unittest
from Args import Par
import pandas as pd
from pandas.testing import assert_frame_equal
import logging

logging.basicConfig(
    filename="file.log", format="%(asctime)s %(levelname)s %(message)s", filemode="a"
)

# Creating an object
logger = logging.getLogger()

class TestPar(unittest.TestCase):
    def test_file_validation_valid(self): #Test for File
        self.parser = Par()
        # Provide a valid CSV file for testing
        valid_file = "weather_1.csv"
        df1 = pd.read_csv(valid_file, sep=",")
        df = self.parser.file_validation(valid_file)
        self.assertIsInstance(df, pd.DataFrame)
        # Check if the structure and data of the DataFrames are equal
        assert_frame_equal(df, df1)
    
    def test_max_validation_valid(self): #Test for Max
        self.parser=Par()
        data = [['tom', 10], ['nick', 15], ['juli', 14]] 
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        x=self.parser.max_value1(df,'Age')
        self.assertEqual(x,15)
    
    def test_max_validation_valid(self): #Test for Min
        self.parser=Par()
        data = [['tom', 10], ['nick', 15], ['juli', 14]] 
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        x=self.parser.min_value1(df,'Age')
        self.assertEqual(x,10)
    
    def test_max_validation_valid(self): #Test for Mean
        self.parser=Par()
        data = [['tom', 10,1], ['nick', 15,2], ['juli', 14,3]] 
        df = pd.DataFrame(data, columns=['Name', 'Age','Num'])
        x=self.parser.mean_value(df,['Age','Num'],False)
        self.assertEqual(x,(13.0,2.0))

if __name__ == '__main__':
    logger.info('in main')
    unittest.main()
