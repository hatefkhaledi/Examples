from graphviz import Digraph

# Create a new directed graph
flowchart = Digraph(comment='CFD Hydrodynamic Simulation Workflow')

# Start
flowchart.node('Start', 'Start')

# 1. Project Planning and Setup
flowchart.node('1', '1. Project Planning and Setup')
flowchart.node('1a', 'Define Objectives')
flowchart.node('1b', 'Select CFD Software')
flowchart.node('1c', 'Establish Simulation Parameters')

flowchart.edge('Start', '1')
flowchart.edge('1', '1a')
flowchart.edge('1a', '1b')
flowchart.edge('1b', '1c')

# 2. Geometry Creation and Pre-processing
flowchart.node('2', '2. Geometry Creation and Pre-processing')
flowchart.node('2a', 'Create/Import Geometry (CAD)')
flowchart.node('2b', 'Simplify Geometry')
flowchart.node('2c', 'Define Computational Domain')
flowchart.node('2d', 'Generate and Refine Mesh')
flowchart.node('2e', 'Mesh Independence Study')

flowchart.edge('1c', '2')
flowchart.edge('2', '2a')
flowchart.edge('2a', '2b')
flowchart.edge('2b', '2c')
flowchart.edge('2c', '2d')
flowchart.edge('2d', '2e')

# 3. Physics Setup
flowchart.node('3', '3. Physics Setup')
flowchart.node('3a', 'Set Fluid Properties')
flowchart.node('3b', 'Select Flow/Turb')
