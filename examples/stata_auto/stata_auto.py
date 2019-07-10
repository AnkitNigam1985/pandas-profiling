import pandas as pd
import pandas_profiling


if __name__ == "__main__":
    # Suggested by @adamrossnelson
    df = pd.read_stata("http://www.stata-press.com/data/r15/auto2.dta")

    # Length left out due to correlation with weight.
    report = pandas_profiling.ProfileReport(df, title="1978 Automobile dataset")
    report.to_file("stata_auto_report.html")

    # Pass rejected variables to new profile report.
    # rejected = pandas_profiling.ProfileReport(df).get_rejected_variables(threshold=0.9)
    # pandas_profiling.ProfileReport(df[rejected])
