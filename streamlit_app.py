import streamlit as st
from graphviz import Digraph

def draw_flowchart():
    # Create a new Graphviz Digraph
    dot = Digraph()

    # Add nodes to the flowchart
    dot.node('Step1', 'Step 1: Pre-processing')
    dot.node('Step2', 'Step 2: Feature Engineering')
    dot.node('Step3', 'Step 3: Model Training')
    dot.node('Step4', 'Step 4: Model Evaluation')
    dot.node('Step5', 'Step 5: Predictions')

    # Add edges between the nodes
    dot.edge('Step1', 'Step2')
    dot.edge('Step2', 'Step3')
    dot.edge('Step3', 'Step4')
    dot.edge('Step4', 'Step5')

    # Render the flowchart
    st.graphviz_chart(dot.source)

# Set up a title for your app
st.title("Code Recipe Flowchart")

# Call the draw_flowchart function to generate and display the flowchart
draw_flowchart()
