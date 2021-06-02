import numpy as np
import pandas as pd

try:
    frame = pd.DataFrame()

    ## Obtaining data from user

    stud_n = int(input("Enter the number of students:"))

    if stud_n == 0:
        raise Exception("You have entered 0 students, you can't go any further...")

    for i in range(stud_n):
        sname = input("Enter the name of student {} : ".format(i + 1))
        data = {
            "Name": sname.title(),
            "S1": np.nan,
            "S2": np.nan,
            "S3": np.nan,
            "S4": np.nan,
            "S5": np.nan,
            "Total": np.nan,
        }
        s = []

        num = int(input("Enter the number of subject for student's marks evaluation: "))

        if num > 5:
            raise Exception("You can only add marks of 5 subjects....")

        c = input("Enter the marks and differentiate with the help of space: ")
        s = [int(x) for x in c.split()]

        if len(s) > num:
            raise Exception(
                "You have entered marks of subjects more than specified number...."
            )
        elif len(s) < num:
            raise Exception(
                "You have entered marks of subjects less than specified number...."
            )

        for j in range(num):
            data["S" + str(j + 1)] = s[j]

        ## creating a dataframe from user data

        frame_col = list(data.keys())
        for counter in range(len(frame_col)):
            frame.loc[i + 1, frame_col[counter]] = data[frame_col[counter]]
        frame.loc[i + 1, "Total"] = np.sum(frame.loc[i + 1, "S1":"Total"])

except Exception as e:
    print(e)
