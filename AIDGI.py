import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Streamlit App
st.set_page_config(page_title="AI Disruption and Growth Index (AIDGI)", layout="wide")

# About This App section at the top
st.markdown("""
## About This App

This app was created for the Sequoia Summer Internship application to showcase my skills in data analysis, interactive visualization, and understanding AI's impact on industries.

### Key Points

1. **Metrics**: AI Adoption Rate, Efficiency Improvement, Revenue Growth, Market Size, and Growth Potential.
2. **Analysis**: AIDGI is calculated using a weighted sum of these metrics, adjustable dynamically.
3. **Visualizations**: Explore AI's impact across industries through bar charts, scatter plots, and pie charts.

### Skills Demonstrated

- **Technical**: Proficient in Python, data analysis with pandas, and visualizations with Plotly.
- **Communication**: Clear explanation of complex concepts.
- **Passion**: Deep interest in AI and technology's transformative potential.

Looking forward to contributing my skills and passion to the Sequoia team.

Best regards,
Muchiri Kahwai
""")

# Sample data based on extracted insights
data = {
    'Industry': ['Healthcare', 'Finance', 'Retail', 'Manufacturing', 'Transportation', 'Education', 'Entertainment'],
    'AI_Adoption': [75, 80, 70, 65, 60, 55, 50],  # Percentage
    'Efficiency_Improvement': [30, 35, 25, 20, 15, 10, 20],  # Percentage
    'Revenue_Growth': [20, 25, 15, 10, 5, 5, 10],  # Percentage
    'Market_Size': [200, 180, 150, 170, 140, 120, 130],  # Billion USD
    'Growth_Potential': [90, 85, 80, 75, 70, 65, 60]  # Percentage
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

# Custom CSS for better styling in both light and dark modes
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--text-color);
        }
        .header {
            font-size: 1.75rem;
            color: var(--text-color);
            margin-top: 20px;
        }
        .subheader {
            font-size: 1.25rem;
            color: var(--text-color);
            margin-top: 10px;
        }
        .css-145kmo2 {
            background-color: var(--background-color);
        }
        :root {
            --text-color: #003366;
            --background-color: #f0f0f5;
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --text-color: #ffffff;
                --background-color: #333333;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">AI Disruption and Growth Index (AIDGI)</div>', unsafe_allow_html=True)

# Detailed Introduction
st.markdown("""
<div class="header">Introduction</div>

AI is transforming industries by improving efficiency, driving revenue growth, and creating new opportunities. 
The AI Disruption and Growth Index (AIDGI) quantifies AI's impact across sectors using key metrics: AI Adoption Rate, Efficiency Improvement, Revenue Growth, Market Size, and Growth Potential.

<div class="subheader">Calculation Method</div>

The AIDGI is a weighted sum of these metrics, adjusted dynamically:
""", unsafe_allow_html=True)

st.latex(r'''
\text{AIDGI} = 0.35 \times \text{AI Adoption Rate} + 0.25 \times \text{Efficiency Improvement} + 0.2 \times \text{Revenue Growth} + 0.1 \times \log(\text{Market Size}) + 0.1 \times \exp(\text{Growth Potential} / 100)
''')

st.markdown("""
### Interactive Elements

Adjust the weights using the sliders in the sidebar to see the impact on AIDGI for each industry.
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

# Display DataFrame with clear metric labels
st.write("## AI Impact Data")
st.dataframe(df.style.format({
    "AI_Adoption": "{:.1f}%",
    "Efficiency_Improvement": "{:.1f}%",
    "Revenue_Growth": "{:.1f}%",
    "Market_Size": "${:,.0f}B",
    "Growth_Potential": "{:.1f}%"
}))

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

# Grouped Bar Chart for Industry Comparison
st.markdown("""
### Industry Comparison: Key Metrics

This grouped bar chart compares key metrics across different industries. The value represents the respective metric's measurement, such as the percentage for AI Adoption, Efficiency Improvement, Revenue Growth, and Growth Potential, and billion USD for Market Size.
""")
fig_grouped = px.bar(df.melt(id_vars=['Industry'], value_vars=['AI_Adoption', 'Efficiency_Improvement', 'Revenue_Growth', 'Market_Size', 'Growth_Potential']),
                     x='Industry', y='value', color='variable', barmode='group',
                     title="Comparison of Key Metrics Across Industries",
                     labels={'value': 'Metric Value', 'variable': 'Metric'},
                     height=400, template='plotly_white')
fig_grouped.update_layout(
    xaxis_title="Industry",
    yaxis_title="Metric Value",
    legend_title_text='Metrics'
)
st.plotly_chart(fig_grouped, use_container_width=True)

# Radar Chart for AI Adoption and Growth Potential
st.markdown("### Radar Chart: AI Adoption and Growth Potential")
fig_radar = go.Figure()

for industry in df['Industry']:
    fig_radar.add_trace(go.Scatterpolar(
        r=df[df['Industry'] == industry][['AI_Adoption', 'Growth_Potential']].values.flatten(),
        theta=['AI_Adoption', 'Growth_Potential'],
        fill='toself',
        name=industry
    ))

fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=True,
    title="AI Adoption and Growth Potential by Industry"
)

st.plotly_chart(fig_radar, use_container_width=True)

# Scatter Plot for AI Adoption vs Efficiency Improvement
st.markdown("### Scatter Plot: AI Adoption vs Efficiency Improvement")
fig_scatter = px.scatter(df, x='AI_Adoption', y='Efficiency_Improvement', color='Industry',
                         title="AI Adoption vs Efficiency Improvement",
                         labels={'AI_Adoption': 'AI Adoption (%)', 'Efficiency_Improvement': 'Efficiency Improvement (%)'},
                         height=400)
st.plotly_chart(fig_scatter, use_container_width=True)

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
st.dataframe(filtered_df.style.format({
    "AI_Adoption": "{:.1f}%",
    "Efficiency_Improvement": "{:.1f}%",
    "Revenue_Growth": "{:.1f}%",
    "Market_Size": "${:,.0f}B",
    "Growth_Potential": "{:.1f}%"
}))

# Detailed Bar Charts
fig2 = px.bar(filtered_df.melt(id_vars=["Industry"], value_vars=["AI_Adoption", "Efficiency_Improvement", "Revenue_Growth", "Market_Size", "Growth_Potential"]),
              x='variable', y='value',
              title=f"Detailed Metrics for {industry}",
              labels={'variable': 'Metric', 'value': 'Metric Value'},
              template='plotly_white')

st.plotly_chart(fig2, use_container_width=True)

# Conclusion Section
st.markdown("""
## Conclusion

The AI Disruption and Growth Index (AIDGI) provides valuable insights into the impact of AI across various industries. By considering key metrics such as AI Adoption, Efficiency Improvement, Revenue Growth, Market Size, and Growth Potential, the AIDGI offers a comprehensive view of how AI is transforming different sectors.

### Key Insights

- **Finance and Healthcare**: These industries show the highest AI Adoption rates, indicating a strong integration of AI technologies.
- **Manufacturing and Transportation**: Significant improvements in efficiency and market size reflect the transformative potential of AI in these sectors.
- **Education and Entertainment**: These industries have lower AI Adoption rates but show promising growth potential.

### Recommendations

- **Focus on High Impact Sectors**: Investments and efforts should be concentrated on industries with high AI Adoption and growth potential.
- **Address Adoption Barriers**: For industries with lower AI Adoption, identify and address barriers to encourage wider adoption of AI technologies.
- **Monitor Trends**: Continuously monitor AI trends and update the AIDGI to reflect the latest developments and shifts in the industry landscape.

I look forward to the opportunity to bring my skills and passion for technology to the Sequoia team.

Best regards,
Muchiri Kahwai
""")
