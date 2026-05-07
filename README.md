Student Grade Prediction
    # This project predicts student final grades.

DATASET
    # Reference: https://www.kaggle.com/code/prajwalkanade/student-grade-prediction

PROCESS
    1.) Data Preprocessing
        # removed outliers using IQR method
        # filtered invalid G3 values
        # grouped absences into categories
        # converted yes/no values to 1/0
        # reset dataset index

    2.) EDA
        # plotted G1 vs G3
        # plotted G2 vs G3
        # used count plots for features

    3.) Models
        # used Linear Regression
        # used Random Forest Regressor

    4.) Evaluate
        # Linear Regression:
            MAE: 0.6765674355716766
            RMSE: 0.8559805562695452
            R2: 0.9219678317859334

        # Random Forest:
            MAE:  0.7267272727272729
            RMSE:  0.8970324814226477
            R2:  0.9143036720180256
    # Therefore, comparing the two models, Linear Regression performed better.

