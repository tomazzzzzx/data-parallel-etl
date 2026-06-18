import polars as pl

class Pipeline:
    def __init__(self): self.steps = []
    def read(self, p): self.steps.append(("read",p)); return self
    def filter(self, e): self.steps.append(("filter",e)); return self
    def write(self, p): self.steps.append(("write",p)); return self
    def execute(self):
        df = None
        for op,a in self.steps:
            if op=="read": df = pl.read_parquet(a)
            elif op=="filter": df = df.filter(a)
            elif op=="write": df.write_parquet(a)
        return df
