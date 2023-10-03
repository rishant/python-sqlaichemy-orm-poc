from sqlalchemy import create_engine, text

if __name__ == '__main__':
    db_url = 'mysql+pymysql://root:root@localhost:3306/shopping'
    engine = create_engine(db_url)

    data_list = []
    with engine.connect() as connection:
        select_query = text('SELECT * FROM shopping.customers')
        result = connection.execute(select_query)
        # Get the column names from the result object's keys() method
        column_names = result.keys()
        for row in result:
            # print(f' row: {row}')
            row_obj = dict(zip(column_names, row))
            print(f' row: {row_obj}')
            data_list.append(row_obj)
        result.close()
    # Now, 'data_list' contains the result of the SELECT query as a list of dictionaries
    print(data_list)
