import pandas as pd
import streamlit as st
import altair as alt

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="RCLCO Financals", page_icon=":bar_chart:", layout="wide")

@st.cache_data
def get_data_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name='FinancialData')  # Replace 'Sheet1' with the correct sheet name if needed
    df['Month'] = pd.to_datetime(df['Month'])
    df.columns = [col.replace('\xa0', ' ') for col in df.columns]  # Replace non-breaking space character with a regular space character
    return df

def create_chart(df, asset, metrics):
    filtered_df = df[df["Asset"] == asset]
    layers = []

    colors = {
        "Revenue": "#1f77b4",
        "Expenses": "#ff7f0e",
        "Income": "#2ca02c",
        "FMV Adjustment": "#1f77b4"
    }

    for metric in metrics:
        if metric in df.columns:
            chart = alt.Chart(filtered_df).mark_bar().encode(
                x="Month:T",
                y=f"{metric}:Q",
                color=alt.value(colors[metric]),
            )
            layers.append(chart)

    final_chart = alt.layer(*layers).resolve_scale(y='independent')
    return final_chart

def main():
    st.title("Financial Charts Comparison")

    file_path = "/Users/ahmedshaker/Downloads/financial_data.xlsx"
    df = get_data_from_excel(file_path)

    # Create columns for sidebars with an empty column in the middle for spacing
    left_sidebar, empty1, empty2, empty3, right_sidebar = st.columns([120, 10, 10, 10, 120])

    asset1 = left_sidebar.selectbox("Select Asset 1", options=df["Asset"].unique())
    asset2 = right_sidebar.selectbox("Select Asset 2", options=df["Asset"].unique())

    metrics = ["Revenue", "Expenses", "Income", "FMV Adjustment"]

    # Add checkboxes to the sidebars
    metrics1 = [metric for metric in metrics if left_sidebar.checkbox(f"{metric} (Asset 1)", key=f"metric1_{metric}")]
    metrics2 = [metric for metric in metrics if right_sidebar.checkbox(f"{metric} (Asset 2)", key=f"metric2_{metric}")]

    # Create charts
    chart1 = create_chart(df, asset1, metrics1).properties(width=500)
    chart2 = create_chart(df, asset2, metrics2).properties(width=500)

    chart_columns = st.columns([1, .1, .1, 1])
    chart_columns[0].altair_chart(chart1, use_container_width=False)
    chart_columns[3].altair_chart(chart2, use_container_width=False)

if __name__ == "__main__":
    main()
