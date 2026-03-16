import pandas as pd
from database.db_config import get_connection  # your config file from earlier


#=======Bulk data upload with less time==========#
# conn = get_connection()
# cursor = conn.cursor()


# # Load Excel file
# # df = pd.read_csv("D:\code\Project\car_ai_assistant\data\BMW_Inventory.csv", encoding="latin1")
# df = pd.read_csv("D:/code/Project/car_ai_assistant/data/BMW_Inventory.csv",
#                   encoding="latin1"
#                   )


# print(df.head())
# print("CSV Loaded Successfully")
# print("Total rows:", len(df))

# # 🔧 Fix NaN values
# df = df.replace({pd.NA: None})
# df = df.where(pd.notnull(df), None)

# # Drop table if exists
# # cursor.execute('DROP TABLES IF EXISTS car_data')
# # cursor.execute('DROP TABLES IF EXISTS cars_data')
# # cursor.execute("DROP TABLE IF EXISTS cars_inventory_data")

# # Create table
# create_table = """
# CREATE TABLE cars_data (
#     Id INT AUTO_INCREMENT PRIMARY KEY,
#     model TEXT,
#     year INT,
#     price INT,
#     transmission VARCHAR(20),
#     mileage INT,
#     fuelType VARCHAR(20),
#     tax INT,
#     mpg FLOAT,
#     engineSize FLOAT
# );
# """
# cursor.execute(create_table)

# # Prepare Insert query
# insert_query = """
# INSERT INTO cars_data
# (model, year, price, transmission, mileage, fueltype, tax, mpg, enginesize)
# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
# """

# # Convert dataframe to list of tuples
# # data = list(df[['model','year','price','transmission','mileage','fuelType','tax','mpg','engineSize']].itertuples(index=False, name=None))

# print("Starting bulk upload...")

# data = []

# for _, row in df.iterrows():
#     data.append(tuple(None if pd.isna(x) else x for x in row))

# # Bulk insert
# cursor.executemany(insert_query, data)

# # Commit
# conn.commit()

# print("✅ CSV data uploaded successfully! Total rows inserted: {cursor.rowcount}")

# # Verify
# cursor.execute("SELECT COUNT(*) FROM cars_inventory_data")
# result = cursor.fetchone()
# print("Rows currently in table:", result[0])

# cursor.close()
# conn.close()

#==============Normal upload its take time==========#
conn = get_connection()
cursor = conn.cursor()


# Load Excel file
# df = pd.read_csv("D:\code\Project\car_ai_assistant\data\BMW_Inventory.csv", encoding="latin1")
df = pd.read_csv("D:/code/Project/car_ai_assistant/data/BMW_Inventory.csv",
                  encoding="latin1"
                  )


print(df.head())
print("CSV Loaded Successfully")
print("Total rows:", len(df))


# Drop table if exists
# cursor.execute('DROP TABLES IF EXISTS car_data')
# cursor.execute('DROP TABLES IF EXISTS cars_data')
cursor.execute("DROP TABLE IF EXISTS car_inventory_data")

# Create table
create_table = """
CREATE TABLE car_inventory_data (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    model TEXT,
    year INT,
    price INT,
    transmission VARCHAR(20),
    mileage INT,
    fuelType VARCHAR(20),
    tax INT,
    mpg FLOAT,
    engineSize FLOAT
);
"""
cursor.execute(create_table)

# Prepare Insert query
insert_query = """
INSERT INTO car_inventory_data
(model, year, price, transmission, mileage, fueltype, tax, mpg, enginesize)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

count = 0
# Insert data row by row
for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row['model'],
        row['year'],
        row['price'],
        row['transmission'],
        row['mileage'],
        row['fuelType'],
        row['tax'],
        row['mpg'],
        row['engineSize']
    ))

    count += 1

    # Show progress every 500 rows
    if count % 50 == 0:
        print(f"Inserted {count} rows...")

# Commit
conn.commit()

print("✅ CSV data uploaded successfully! Total rows inserted: {cursor.rowcount}")

# # Verify
# cursor.execute("SELECT COUNT(*) FROM cars_inventory_data")
# result = cursor.fetchone()
# print("Rows currently in table:", result[0])

cursor.close()
conn.close()