import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Sample data based on extracted insights
data = {
    'Industry': ['Healthcare', 'Finance', 'Retail', 'Manufacturing', 'Transportation', 'Education', 'Entertainment'],
    'AI_Adoption': [75, 80, 70, 65, 60, 55, 50],
    'Efficiency_Improvement': [30, 35, 25, 20, 15, 10, 20],
    'Revenue_Growth': [20, 25, 15, 10, 5, 5, 10],
    'Market_Size': [200, 180, 150, 170, 140, 120, 130],
    'Growth_Potential': [90, 85, 80, 75, 70, 65, 60]
}

df = pd.DataFrame(data)

# Calculate AIDGI with updated formula
def calculate_aidgi(row, ai_weight, eff_weight, rev_weight, market_weight, growth_weight):
    return (
        ai_weight * row['AI_Adoption'] +
        eff_weight * row['Efficiency_Improvement'] +
        rev_weight * row['Revenue_Growth'] +
        market_weight * np.log(row['Market_Size']) +
        growth_weight * np.exp(row['Growth_Potential'] / 100)
    )

# Streamlit App
st.set_page_config(page_title="AI Disruption and Growth Index (AIDGI)", layout="wide")

st.title("AI Disruption and Growth Index (AIDGI)")

# Detailed Introduction
st.markdown("""
## Introduction

AI is transforming various industries by improving efficiency, driving revenue growth, and creating new opportunities for growth. 
To understand and quantify the impact of AI across different sectors, I have developed the AI Disruption and Growth Index (AIDGI). 
The AIDGI is a composite score that reflects the level of AI disruption and growth potential in various industries based on several key factors.

### Factors Considered

1. **AI Adoption Rate**: This factor measures how widely AI technologies are being adopted in an industry. A higher adoption rate indicates a greater integration of AI solutions, leading to significant transformations.
2. **Efficiency Improvement**: AI often leads to better efficiency through automation, optimization, and enhanced decision-making. This factor captures the extent of efficiency gains attributed to AI.
3. **Revenue Growth**: AI can drive substantial revenue growth by creating new products, services, and business models. This factor measures the impact of AI on revenue expansion.
4. **Market Size**: The size of the market in which AI is being deployed is crucial. Larger markets have more opportunities for AI to create value. I use a logarithmic scale for market size to reflect its impact proportionately.
5. **Growth Potential**: This factor considers the future potential for growth driven by AI. It is measured using an exponential scale to emphasize industries with high growth prospects.

### Calculation Method

The AIDGI is calculated using a weighted sum of these factors, with specific weights assigned to each factor based on its importance. The formula is:
""")

st.latex(r'''
\text{AIDGI} = 0.35 \times \text{AI Adoption Rate} + 0.25 \times \text{Efficiency Improvement} + 0.2 \times \text{Revenue Growth} + 0.1 \times \log(\text{Market Size}) + 0.1 \times \exp(\text{Growth Potential} / 100)
''')

st.markdown("""
### Interactive Elements

You can adjust the weights of each factor using the sliders in the sidebar to see how they impact the AIDGI for each industry. This dynamic adjustment helps you explore different scenarios and understand the sensitivity of the index to various factors.
""")

# Sidebar for weight adjustments
st.sidebar.header("Adjust Weights")
ai_weight = st.sidebar.slider("AI Adoption Rate Weight", 0.0, 1.0, 0.35, 0.01)
eff_weight = st.sidebar.slider("Efficiency Improvement Weight", 0.0, 1.0, 0.25, 0.01)
rev_weight = st.sidebar.slider("Revenue Growth Weight", 0.0, 1.0, 0.20, 0.01)
market_weight = st.sidebar.slider("Market Size Weight", 0.0, 1.0, 0.10, 0.01)
growth_weight = st.sidebar.slider("Growth Potential Weight", 0.0, 1.0, 0.10, 0.01)

# Normalize weights
total_weight = ai_weight + eff_weight + rev_weight + market_weight + growth_weight
ai_weight /= total_weight
eff_weight /= total_weight
rev_weight /= total_weight
market_weight /= total_weight
growth_weight /= total_weight

# Calculate AIDGI for each industry
df['AIDGI'] = df.apply(calculate_aidgi, axis=1, args=(ai_weight, eff_weight, rev_weight, market_weight, growth_weight))
df.sort_values(by='AIDGI', ascending=False, inplace=True)

# Display DataFrame with styling
st.write("## AI Impact Data")
st.dataframe(df.style.background_gradient(cmap='viridis'))

# Interactive Bar Chart for AIDGI
fig = px.bar(df, x='Industry', y='AIDGI',
             title="AI Disruption and Growth Index (AIDGI) Across Industries",
             labels={'AIDGI': 'AIDGI Score'},
             height=400, color='Industry', template='plotly_dark')

# Show Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Additional Interactive Elements
st.markdown("### Select an Industry to View Detailed Metrics")
with st.container():
    st.markdown("""
    <div class="dropdown-container">
        <strong>Select Industry:</strong>
    """, unsafe_allow_html=True)
    industry = st.selectbox('', df['Industry'], label_visibility='collapsed')
    st.markdown("</div>", unsafe_allow_html=True)

filtered_df = df[df['Industry'] == industry]

st.write(f"## Detailed View for {industry}")
st.dataframe(filtered_df.style.background_gradient(cmap='coolwarm'))

# Detailed Bar Charts
fig2 = px.bar(filtered_df.melt(id_vars=["Industry"], value_vars=["AI_Adoption", "Efficiency_Improvement", "Revenue_Growth", "Market_Size", "Growth_Potential"]),
              x='variable', y='value',
              title=f"Detailed Metrics for {industry}",
              labels={'variable': 'Metric', 'value': 'Value'},
              template='plotly_white')

st.plotly_chart(fig2, use_container_width=True)
