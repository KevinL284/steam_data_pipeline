import pandas as pd

def dataframe_to_json(df):
  """
  Convertendo o DF em formato JSON serializdo
  """

  return(
    df.astype(object)
    .where(pd.notnull(df), None)
    .to_dict(orient="records")
  )
