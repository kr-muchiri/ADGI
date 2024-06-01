import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# About This App section at the top
st.markdown("""
## About This App

This app was created as part of my application for the Sequoia Summer Internship Opportunity. It demonstrates my technical skills in data analysis, interactive visualization, and understanding of AI's impact on various industries.

### Thought Process

1. **Identifying Key Metrics**: The key metrics considered for evaluating AI's impact include AI Adoption Rate, Efficiency Improvement, Revenue Growth, Market Size, and Growth Potential.
2. **Weighted Analysis**: The AI Disruption and Growth Index (AIDGI) is calculated using a weighted sum of these factors, with the ability to adjust weights dynamically.
3. **Interactive Visualizations**: Users can explore the impact of AI across different industries through interactive bar charts, heatmaps, and pie charts.

### Skills Demonstrated

- **Technical Background**: Proficiency in Python, data analysis with pandas, and interactive visualizations with Plotly and Seaborn.
- **Clear Communication**: Clear and concise explanations of complex concepts, both in the app and in accompanying documentation.
- **Passion for Technology**: A deep interest in how AI and technology are transforming industries and the potential for future growth.

I look forward to the opportunity to bring my skills and passion for technology to the Sequoia team.

Best regards,
Muchiri Kahwai
""")

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #003366;
        }
        .header {
            font-size: 1.75rem;
            color: #003366;
            margin-top: 20px;
        }
        .subheader {
            font-size: 1.25rem;
            color: #003366;
            margin-top: 10px;
        }
        .css-145kmo2 {
            background-color: #f0f0f5;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">AI Disruption and Growth Index (AIDGI)</div>', unsafe_allow_html=True)

# Detailed Introduction
st.markdown("""
<div class="header">Introduction</div>

AI is transforming various industries by improving efficiency, driving revenue growth, and creating new opportunities for growth. 
To understand and quantify the impact of AI across different sectors, I have developed the AI Disruption and Growth Index (AIDGI). 
The AIDGI is a composite score that reflects the level of AI disruption and growth potential in various industries based on several key factors.

<div class="subheader">Factors Considered</div>

1. **AI Adoption Rate**: Measures how widely AI technologies are being adopted in an industry.
2. **Efficiency Improvement**: Captures the extent of efficiency gains attributed to AI.
3. **Revenue Growth**: Measures the impact of AI on revenue expansion.
4. **Market Size**: Reflects the size of the market in which AI is being deployed, using a logarithmic scale.
5. **Growth Potential**: Considers the future potential for growth driven by AI, using an exponential scale.

<div class="subheader">Calculation Method</div>

The AIDGI is calculated using a weighted sum of these factors, with specific weights assigned to each factor based on its importance. The formula is:
""", unsafe_allow_html=True)

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

# Display DataFrame without styling
st.write("## AI Impact Data")
st.dataframe(df)

# Interactive Bar Chart for AIDGI
fig = px.bar(df, x='Industry', y='AIDGI',
             title="AI Disruption and Growth Index (AIDGI) Across Industries",
             labels={'AIDGI': 'AIDGI Score'},
             height=400, color='Industry', template='plotly_dark')

# Show Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Additional Visualizations
st.markdown("### Weight Distribution")
labels = ['AI Adoption Rate', 'Efficiency Improvement', 'Revenue Growth', 'Market Size', 'Growth Potential']
values = [ai_weight, eff_weight, rev_weight, market_weight, growth_weight]
fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig_pie.update_layout(title_text='Weight Distribution for AIDGI Calculation')
st.plotly_chart(fig_pie, use_container_width=True)

# Heatmap for Industry Comparison
st.markdown("### Industry Comparison Heatmap")
heatmap_data = df.set_index('Industry').T
fig_heatmap, ax = plt.subplots()
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", ax=ax)
ax.set_title('Comparison of AI Metrics Across Industries')
st.pyplot(fig_heatmap)

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
st.dataframe(filtered_df)

# Detailed Bar Charts
fig2 = px.bar(filtered_df.melt(id_vars=["Industry"], value_vars=["AI_Adoption", "Efficiency_Improvement", "Revenue_Growth", "Market_Size", "Growth_Potential"]),
              x='variable', y='value',
              title=f"Detailed Metrics for {industry}",
              labels={'variable': 'Metric', 'value': 'Value'},
              template='plotly_white')

st.plotly_chart(fig2, use_container_width=True)
