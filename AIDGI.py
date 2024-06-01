import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Streamlit App
st.set_page_config(page_title="AI Disruption and Growth Index (AIDGI)", layout="wide")


# Display the Sequoia logo
st.image("sequoia_logo.png", width=400)  

# About This App section at the top
st.markdown("""
## About This App

Welcome to the AI Disruption and Growth Index (AIDGI) app! This application was developed as part of my application for the Sequoia Summer Internship Opportunity. It showcases my technical skills in data analysis, interactive visualization, and my understanding of AI's transformative impact on various industries.

### Key Points

1. **Metrics Selection**: The key metrics chosen to evaluate AI's impact include AI Adoption Rate, Efficiency Improvement, Revenue Growth, Market Size, and Growth Potential.
2. **Weighted Analysis**: The AIDGI is computed using a weighted sum of these metrics. The weights can be adjusted dynamically to explore different scenarios.
3. **Interactive Visualizations**: The app features interactive bar charts, scatter plots, and pie charts to help visualize AI's impact across industries.

### Skills Demonstrated

- **Technical Proficiency**: Expertise in Python, data analysis with pandas, and creating interactive visualizations with Plotly.
- **Clear Communication**: Ability to explain complex concepts in a clear and concise manner.
- **Passion for Technology**: A strong interest in how AI and technology are reshaping industries and creating opportunities for growth.



**Date Built**: May 31, 2024
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
        body {
            background-color: var(--background-color);
            color: var(--text-color);
        }
        .main {
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

AI is revolutionizing industries by enhancing efficiency, driving revenue growth, and opening new avenues for innovation. 
The AI Disruption and Growth Index (AIDGI) is designed to quantify the impact of AI across different sectors. It aggregates key metrics to provide a comprehensive view of AI's transformative potential.

### Key Metrics

1. **AI Adoption Rate**: The percentage of companies within an industry adopting AI technologies.
2. **Efficiency Improvement**: The percentage increase in efficiency due to AI implementation.
3. **Revenue Growth**: The percentage increase in revenue attributed to AI.
4. **Market Size**: The size of the industry market in billions of USD, evaluated on a logarithmic scale.
5. **Growth Potential**: The projected growth potential driven by AI, expressed as a percentage.

### Calculation Method

The AIDGI is computed using a weighted sum of these metrics. The weights reflect the relative importance of each factor and can be adjusted dynamically:

""", unsafe_allow_html=True)

st.latex(r'''
\text{AIDGI} = 0.35 \times \text{AI Adoption Rate} + 0.25 \times \text{Efficiency Improvement} + 0.2 \times \text{Revenue Growth} + 0.1 \times \log(\text{Market Size}) + 0.1 \times \exp(\text{Growth Potential} / 100)
''')

st.markdown("""
### Rationale Behind the Metrics and Formula

The chosen metrics and their weights are based on a comprehensive analysis of the factors that significantly impact AI's transformative potential in various industries:

- **AI Adoption Rate**: A higher adoption rate indicates that more companies are leveraging AI, which generally leads to greater overall industry transformation. This metric has the highest weight (0.35) to reflect its importance.
- **Efficiency Improvement**: AI's ability to enhance efficiency is a critical driver of its value proposition. Improvements in efficiency lead to cost savings and better resource utilization, which is why this metric is given a weight of 0.25.
- **Revenue Growth**: The impact of AI on revenue growth is a direct indicator of its economic benefits. Although crucial, it is weighted at 0.20 to balance its influence with other factors.
- **Market Size**: Larger markets provide more opportunities for AI to make a significant impact. Using the logarithm of market size helps normalize the scale and ensures that industries with extremely large markets do not disproportionately influence the index. This metric is weighted at 0.10.
- **Growth Potential**: This metric captures the future prospects of AI in an industry. By using an exponential scale, we emphasize the significance of high growth potential in driving future transformations. This metric is also weighted at 0.10.

By combining these metrics with their respective weights, the AIDGI provides a balanced and comprehensive view of how AI is disrupting and driving growth across different sectors.

### Data Sources

The data used in this app is derived from reputable industry reports and insights, including:

- [McKinsey's State of AI Report](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Deloitte's State of AI in the Enterprise](https://www2.deloitte.com/content/dam/Deloitte/us/Documents/consulting/us-state-of-gen-ai-report-q2.pdf)
- [PwC's AI Study](https://www.pwc.com/gx/en/issues/data-and-analytics/publications/artificial-intelligence-study.html)
- [KPMG's AI Insights](https://kpmg.com/be/en/home/insights/2023/07/ai-insights.html)
- [OECD's AI Policy Observatory](https://www.oecd.org/digital/artificial-intelligence/)
- [Bank of America's AI Economic Impact](https://business.bofa.com/en-us/content/economic-impact-of-ai.html)

### Note on Data Estimates

The data provided here are rough estimates due to time constraints. A more robust model with precise data would be built for more accurate analysis, but these estimates serve as a foundational stepping stone for this demonstration.

### Interactive Elements

Use the sliders in the sidebar to adjust the weights of each metric and see how they influence the AIDGI for each industry. This interactivity allows for exploring different scenarios and understanding the sensitivity of the index to various factors.
""")

# Sidebar for weight adjustments
st.sidebar.header("Adjust Weights")

# Initialize weights with state management
if 'weights' not in st.session_state:
    st.session_state.weights = {
        'AI Adoption Rate': 0.35,
        'Efficiency Improvement': 0.25,
        'Revenue Growth': 0.20,
        'Market Size': 0.10,
        'Growth Potential': 0.10
    }

def update_weights(new_values):
    total_weight = sum(new_values.values())
    for key in new_values:
        st.session_state.weights[key] = new_values[key] / total_weight

new_weights = {}
new_weights['AI Adoption Rate'] = st.sidebar.slider("AI Adoption Rate Weight", 0.0, 1.0, st.session_state.weights['AI Adoption Rate'], 0.01)
new_weights['Efficiency Improvement'] = st.sidebar.slider("Efficiency Improvement Weight", 0.0, 1.0, st.session_state.weights['Efficiency Improvement'], 0.01)
new_weights['Revenue Growth'] = st.sidebar.slider("Revenue Growth Weight", 0.0, 1.0, st.session_state.weights['Revenue Growth'], 0.01)
new_weights['Market Size'] = st.sidebar.slider("Market Size Weight", 0.0, 1.0, st.session_state.weights['Market Size'], 0.01)
new_weights['Growth Potential'] = st.sidebar.slider("Growth Potential Weight", 0.0, 1.0, st.session_state.weights['Growth Potential'], 0.01)

update_weights(new_weights)

# Calculate AIDGI for each industry
df['AIDGI'] = df.apply(calculate_aidgi, axis=1, args=(
    st.session_state.weights['AI Adoption Rate'],
    st.session_state.weights['Efficiency Improvement'],
    st.session_state.weights['Revenue Growth'],
    st.session_state.weights['Market Size'],
    st.session_state.weights['Growth Potential']
))
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
values = [
    st.session_state.weights['AI Adoption Rate'],
    st.session_state.weights['Efficiency Improvement'],
    st.session_state.weights['Revenue Growth'],
    st.session_state.weights['Market Size'],
    st.session_state.weights['Growth Potential']
]
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
