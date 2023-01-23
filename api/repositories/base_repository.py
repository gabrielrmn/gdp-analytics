import pandas as pd
from utils import db_utils


class BaseRepository():

    def __init__(self, logger):
        self.engine = db_utils.get_engine()
        self.logger = logger

    def get_country_info(self, country):
        columns_to_select = 'a.country_name, a.country_code, b.region, b.incomegroup, b.tablename, a.indicator_name, a.indicator_code'
        query_filter = f"WHERE a.country_name = '{country}' OR a.country_code = '{country}'"
        join_condition = 'JOIN metadata_country AS b ON b.country_code = a.country_code'
        group_by = 'GROUP BY 1,2,3,4,5,6,7'
        query = f"SELECT {columns_to_select} FROM gdp_by_country AS a {join_condition} {query_filter} {group_by}"

        self.logger.info(f"Getting country information with query: {query}")

        data = pd.read_sql(query, self.engine)

        return data.to_json(orient='records')

    def get_countries_by_region(self, region):
        columns_to_select = 'a.country_name AS country_name, a.country_code, b.region, a.year, a.value'
        query_filter = f"WHERE UPPER(b.region) = '{region}'"
        join_condition = 'JOIN metadata_country AS b ON b.country_code = a.country_code'
        order_by = 'ORDER BY 3, 1, 4'
        query = f"SELECT {columns_to_select} FROM gdp_by_country AS a {join_condition} {query_filter} {order_by}"

        self.logger.info(
            f"Getting GDP information for region {region} with query: {query}")

        data = pd.read_sql(query, self.engine)
        data = data.pivot_table(values=['value'], index=[
                                'country_code', 'region', 'country_name'], columns=['year'], dropna=True)

        data.columns = data.columns.droplevel(0)
        data = data.reset_index()

        return data.to_json(orient='records')

    def get_country_gdp(self, country):
        columns_to_select = 'a.country_name, a.country_code, a.year, a.value'
        query_filter = f"WHERE a.country_name = '{country}' OR a.country_code = '{country}'"
        query = f"SELECT {columns_to_select} FROM gdp_by_country AS a {query_filter}"

        self.logger.info(
            f"Getting GDP information for country {country} with query: {query}")

        data = pd.read_sql(query, self.engine)
        data = data.pivot_table(values=['value'], index=[
                                'country_name', 'country_code'], columns=['year'], dropna=False)

        data.columns = data.columns.droplevel(0)
        data = data.reset_index()

        return data.to_json(orient='records')

    def get_gdp_avg(self, start_year, end_year, order):
        columns_to_select = 'country_name, country_code, COALESCE(AVG(value), 0) AS avg_gdp'
        query_filter = f"WHERE CAST(year AS INTEGER) BETWEEN {start_year} AND {end_year}"
        group_by = "GROUP BY 1, 2"
        order_by = f"ORDER BY 3 {order}"
        query = f"SELECT {columns_to_select} FROM gdp_by_country AS a {query_filter} {group_by} {order_by} LIMIT 10"

        self.logger.info(f"Getting average gdp with query: {query}")

        data = pd.read_sql(query, self.engine)

        return data.to_json(orient='records')
