import pandas as pd
import numpy as np
import typing


def wrap_in_bigcell(x: typing.Any) -> str:
    if isinstance(x, float) and int(x) == x:
        r = int(x)
    else:
        r = x
    return f"\\bigcell{{l}}{{{r}}}"


def dataframe_to_latex_table(
    df: pd.DataFrame, left_top_item: str = "", caption: typing.Optional[str] = None
) -> str:
    result = ""

    result += r"\begin{table}[H]" + "\n"
    result += r"\centering" + "\n"
    result += (
        r"\begin{tabular}{" + ("c".join(["|"] * (len(df.columns) + 2))) + "} " + "\n"
    )
    result += r"\hline" + "\n"
    result += f"\\bigcell{{l}}{{{left_top_item}}} & "
    result += " & ".join([wrap_in_bigcell(value) for value in df.columns]) + "\\\\\n"

    for row, values in df.iterrows():
        result += "\\hline" + "\n"
        result += wrap_in_bigcell(row)
        result += " & "
        result += " & ".join([wrap_in_bigcell(value) for value in values])
        result += r"\\" + "\n"

    result += r"\hline" + "\n"
    result += r"\end{tabular}" + "\n"
    if caption is not None:
        result += f"\\caption{{{caption}}}" + "\n"
    result += r"\end{table}"

    return result


def array_2d_to_latex(arr: np.ndarray, rounding: int = 4) -> str:
    return (
        r"\begin{table}[H]"
        + "\n"
        + r"\centering"
        + "\n"
        + r"\begin{tabular}{"
        + " ".join(["l"] * arr.shape[0])
        + "}\n"
        + "\\\\\n".join(["& ".join([str(round(n, rounding)) for n in a]) for a in arr])
        + "\\\\\n"
        + r"\end{tabular}"
        + r"\end{table}"
    )
