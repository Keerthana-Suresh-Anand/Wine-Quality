import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            data_cols = set(data.columns)
            schema_cols = set(self.config.all_schema.keys())

            # Check for missing and extra columns
            missing_in_data = schema_cols - data_cols
            extra_in_data = data_cols - schema_cols

            validation_status = not missing_in_data and not extra_in_data

            # Write detailed results
            with open(self.config.STATUS_FILE, "w") as f:
                if validation_status:
                    f.write("Validation status: True\nAll columns match the schema.")
                else:
                    f.write("Validation status: False\n")
                    if missing_in_data:
                        f.write(f"Missing columns in data: {list(missing_in_data)}\n")
                    if extra_in_data:
                        f.write(f"Extra columns in data: {list(extra_in_data)}\n")

            return validation_status

        except Exception as e:
            raise e
