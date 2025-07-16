def add_engineered_features(X):
    X = X.copy()
    X['temp_diff'] = X['Process temperature [K]'] - X['Air temperature [K]']
    X['temp_ratio'] = X['Process temperature [K]'] / X['Air temperature [K]']
    X['torque_to_speed_ratio'] = X['Torque [Nm]'] / X['Rotational speed [rpm]']
    X['power_approx'] = X['Torque [Nm]'] * X['Rotational speed [rpm]'] * 0.10472
    X['high_torque_flag'] = (X['Torque [Nm]'] > 50).astype(int)
    X['low_speed_flag'] = (X['Rotational speed [rpm]'] < 1500).astype(int)
    X['overheat_flag'] = (X['Air temperature [K]'] > 303).astype(int)
    X['air_temp_norm'] = X['Air temperature [K]'] - 300
    X['process_temp_norm'] = X['Process temperature [K]'] - 310
    X['torque_x_wear'] = X['Torque [Nm]'] * X['Tool wear [min]']
    X['speed_x_wear'] = X['Rotational speed [rpm]'] * X['Tool wear [min]']
    X['tempdiff_x_torque'] = X['temp_diff'] * X['Torque [Nm]']
    X['stress_index'] = (X['Torque [Nm]'] ** 2) / X['Rotational speed [rpm]']
    return X