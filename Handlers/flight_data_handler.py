import pandas as pd
from Utils.date_utils import DateUtils
from logger import CustomLogger
LOGGER = CustomLogger.get_logger(__name__)


class FlightDataHandler:
    def __init__(self, file_input_path: str, file_output_path: str, sheet_name=0):
        """
        Read data from an Excel file.

        :param sheet_name: Name or index of the sheet to read (default is 0).
        """
        LOGGER.info("Initializing FlightDataHandler class.")
        self.file_path = file_input_path
        self.file_output_path = file_output_path
        self.sheet_name = sheet_name
        self.df = pd.read_excel(file_input_path, sheet_name)

    @property
    def pending_flight_row(self) -> pd.Series:
        # Find the first row that is not completed
        LOGGER.info("Getting pending flight row..")
        try:
            row_df: pd.Series = self.df[self.df['Status'] == 0].iloc[0]
        except IndexError:
            row_df = pd.Series()
        return row_df

    def get_column_values(self, column_name):
        # Extract and return values from a specific column
        if column_name in self.data.columns:
            return self.data[column_name]

    def update_specific_row(self, row_df):
        LOGGER.info(f"Updating  ID: {row_df.name} row  row data")
        self.df.iloc[row_df.name] = row_df
        self.__update_flight_data()

    def __update_flight_data(self):
        LOGGER.info(f"Updating output xlsx file.")
        # Write the updated DataFrame back to the Excel file
        # Set index=False to avoid writing row numbers as a new column
        try:
            self.df.to_excel(self.file_output_path, index=False)
        except Exception as e:
            LOGGER.error(f"Error writing to Excel: {e}")
