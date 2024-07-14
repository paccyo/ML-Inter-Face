
import pandas as pd


class DS:

    def send(self, data):
        self.load_dataframe(data)

    def load_dataframe(self, data):
        if type(data) == str:
            self.df = pd.read_csv(data)
        elif type(data) == pd.DataFrame:
            self.df = data
        
    def analyze(self):
        pass