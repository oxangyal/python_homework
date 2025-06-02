import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        # Get the length of the DataFrame
        n = len(self)

        # Loop through the DataFrame in chunks of 10 rows
        for start in range(0, n, 10):
            end = min(start + 10, n)
            # Print the column headers
            print(self.columns.to_list())
            # Print the current chunk of rows
            print(super().iloc[start:end])
            print("-----------")

if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()