import pandas as pd
from sqlalchemy import create_engine

db_name = 'postgres'
db_user = 'postgres'
db_pass = 'password'
db_host = 'db'
db_port = '5432'


def get_engine():
    con_str = 'postgresql://{}:{}@{}:{}/{}'.format(
        db_user, db_pass, db_host, db_port, db_name)
    engine = create_engine(
        con_str)
    return engine


def fix_columns_names(df):
    df.columns = map(str.lower, df.columns)
    df.columns = df.columns.str.replace(' ', '_')


def df_to_postgres_table(df, tb_name, engine, index=False, if_exists='replace'):
    df.to_sql(tb_name, engine, index=index, if_exists=if_exists)


# Reading DFs from CSVs
gdp_data = pd.read_csv(
    './data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv', header=2).dropna(axis=1, how='all').melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                                                                                                       var_name='Year',
                                                                                                       value_name='Value')
metadata_country = pd.read_csv(
    './data/Metadata_Country_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv').dropna(axis=1, how='all')

engine = get_engine()

fix_columns_names(gdp_data)
fix_columns_names(metadata_country)

df_to_postgres_table(gdp_data, 'gdp_by_country', engine)
df_to_postgres_table(metadata_country, 'metadata_country', engine)
