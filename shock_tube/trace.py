# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
controlDict = OpenFOAMReader(FileName='\\\\wsl$\\Ubuntu\\home\\jyy2\\OpenFOAM\\jyy2-dev\\run\\shockTube\\system\\controlDict')
controlDict.MeshRegions = ['internalMesh']
controlDict.CellArrays = ['T', 'U', 'mag(U)', 'p', 'rho']

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView1.ViewSize = [400, 400]

# show data in view
controlDictDisplay = Show(controlDict, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
controlDictDisplay.Representation = 'Surface'
controlDictDisplay.ColorArrayName = ['POINTS', 'p']
controlDictDisplay.LookupTable = pLUT
controlDictDisplay.OSPRayScaleArray = 'p'
controlDictDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
controlDictDisplay.SelectOrientationVectors = 'U'
controlDictDisplay.SelectScaleArray = 'p'
controlDictDisplay.GlyphType = 'Arrow'
controlDictDisplay.GlyphTableIndexArray = 'p'
controlDictDisplay.GaussianRadius = 0.05
controlDictDisplay.SetScaleArray = ['POINTS', 'p']
controlDictDisplay.ScaleTransferFunction = 'PiecewiseFunction'
controlDictDisplay.OpacityArray = ['POINTS', 'p']
controlDictDisplay.OpacityTransferFunction = 'PiecewiseFunction'
controlDictDisplay.DataAxesGrid = 'GridAxesRepresentation'
controlDictDisplay.PolarAxes = 'PolarAxesRepresentation'
controlDictDisplay.ScalarOpacityFunction = pPWF
controlDictDisplay.ScalarOpacityUnitDistance = 1.0392304845413265
controlDictDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
controlDictDisplay.ScaleTransferFunction.Points = [8552.599609375, 0.0, 0.5, 0.0, 85526.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
controlDictDisplay.OpacityTransferFunction.Points = [8552.599609375, 0.0, 0.5, 0.0, 85526.0, 1.0, 0.5, 0.0]

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView1, layout=layout1, hint=0)

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
controlDictDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on controlDict
controlDict.MeshRegions = ['empty', 'internalMesh', 'sides']

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=controlDict,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-5.0, -1.0, -1.0]
plotOverLine1.Source.Point2 = [5.0, 1.0, 1.0]

CreateLayout('Layout #2')

# set active view
SetActiveView(None)

# set active source
SetActiveSource(plotOverLine1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['mag(U)', 'p', 'rho', 'T', 'U_Magnitude']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'mag(U)', 'mag(U)', 'p', 'p', 'rho', 'rho', 'T', 'T', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'mag(U)', '0.89', '0.1', '0.11', 'p', '0.22', '0.49', '0.72', 'rho', '0.3', '0.69', '0.29', 'T', '0.6', '0.31', '0.64', 'U_X', '1', '0.5', '0', 'U_Y', '0.65', '0.34', '0.16', 'U_Z', '0', '0', '0', 'U_Magnitude', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'mag(U)', '0', 'p', '0', 'rho', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'mag(U)', '1', 'p', '1', 'rho', '1', 'T', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'mag(U)', '2', 'p', '2', 'rho', '2', 'T', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'mag(U)', '0', 'p', '0', 'rho', '0', 'T', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesMarkerSize = ['arc_length', '4', 'mag(U)', '4', 'p', '4', 'rho', '4', 'T', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout2 = GetLayoutByName("Layout #2")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout2, hint=0)

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['mag(U)', 'p', 'rho', 'U_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'mag(U)', '0.889998', '0.100008', '0.110002', 'p', '0.220005', '0.489998', '0.719997', 'rho', '0.300008', '0.689998', '0.289998', 'T', '0.6', '0.310002', '0.639994', 'U_X', '1', '0.500008', '0', 'U_Y', '0.650004', '0.340002', '0.160006', 'U_Z', '0', '0', '0', 'U_Magnitude', '0.889998', '0.100008', '0.110002', 'vtkValidPointMask', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotOverLine1Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'mag(U)', '0', 'p', '0', 'rho', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'mag(U)', '1', 'p', '1', 'rho', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'mag(U)', '2', 'p', '2', 'rho', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'mag(U)', '0', 'p', '0', 'rho', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'T', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'mag(U)', '4', 'p', '4', 'rho', '4', 'vtkValidPointMask', '4']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['mag(U)', 'p', 'rho']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['p', 'rho']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['rho']

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 20.07639128970739]
renderView1.CameraParallelScale = 5.196152422706632

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).