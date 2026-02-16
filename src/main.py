import pathlib

import polars as pl

from azure_blob import download_blob
from azure_blob import upload_blob

# def build_it():
#     df = pl.DataFrame(
#         {
#             "foo": [1, 2, 3, 4, 5],
#             "bar": [6, 7, 8, 9, 10],
#             "ham": ["a", "b", "c", "d", "e"],
#         }
#     )
#     return df


def main():
    print("Hello from gotham-harbor!")

    # path='/data/my_test.parquet'
    # df = build_it()
    # df.write_parquet(path)
    
    # Download to /data/
    download_blob("gothamstorage", "output.parquet", "/data/my_test.parquet")

    df = pl.read_parquet("/data/my_test.parquet")
    print(df.head())
 
    df = df.with_columns(
       (pl.col("a") * 2).alias("a")
    )
    print(df.head())

    # write then upload 
    df.write_parquet("/lake/output.parquet")
    upload_blob("gothamstorage", "output.parquet", "/lake/output.parquet")



if __name__ == "__main__":
    main()
