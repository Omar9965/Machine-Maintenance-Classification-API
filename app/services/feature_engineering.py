import pandas as pd


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features derived from raw sensor data.

    These features must exactly match those used during model training.
    """
    df = df.copy()

    # Temperature features
    df["temp_diff"] = df["Process temperature [K]"] - df["Air temperature [K]"]
    df["temp_ratio"] = df["Process temperature [K]"] / df["Air temperature [K]"]

    # Mechanical features
    df["torque_to_speed_ratio"] = df["Torque [Nm]"] / df["Rotational speed [rpm]"]
    df["power_approx"] = df["Torque [Nm]"] * df["Rotational speed [rpm]"] * 0.10472

    # Binary flags
    df["high_torque_flag"] = (df["Torque [Nm]"] > 50).astype(int)
    df["low_speed_flag"] = (df["Rotational speed [rpm]"] < 1500).astype(int)
    df["overheat_flag"] = (df["Air temperature [K]"] > 303).astype(int)

    # Normalized temperatures
    df["air_temp_norm"] = df["Air temperature [K]"] - 300
    df["process_temp_norm"] = df["Process temperature [K]"] - 310

    # Interaction features
    df["torque_x_wear"] = df["Torque [Nm]"] * df["Tool wear [min]"]
    df["speed_x_wear"] = df["Rotational speed [rpm]"] * df["Tool wear [min]"]
    df["tempdiff_x_torque"] = df["temp_diff"] * df["Torque [Nm]"]

    # Stress index
    df["stress_index"] = (df["Torque [Nm]"] ** 2) / df["Rotational speed [rpm]"]

    return df
