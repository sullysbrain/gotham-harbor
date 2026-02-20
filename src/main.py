import pathlib
from datetime import datetime, timezone

import polars as pl

from azure_blob import download_blob, upload_blob

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
    # download_blob("gothamlake", "silver/my_test.parquet", "/data/my_test.parquet")

    # df = pl.read_parquet("/data/my_test.parquet")
    # print(df.head())
 
    # df = df.with_columns(
    #    (pl.col("a") * 2).alias("a")
    # )
    # print(df.head())

    # write then upload
    # df.write_parquet("/lake/my_test.parquet")
    # upload_blob("gothamlake", "silver/my_test.parquet", "/lake/my_test.parquet")

    # Append current time to silver/logs.txt
    log_local = "/data/logs.txt"
    try:
        download_blob("gothamlake", "silver/logs.txt", log_local)
        existing = pathlib.Path(log_local).read_text()
    except Exception:
        existing = ""
    updated = existing + datetime.now(timezone.utc).isoformat() + "\n"
    pathlib.Path(log_local).write_text(updated)
    print(f'Updated log file with: {updated}')
    upload_blob("gothamlake", "silver/logs.txt", log_local)








if __name__ == "__main__":
    main()
