import nuke
def RenderMultipleNodes():
    render_information = []
    
    def showChannels():
        return '\n'.join(render_information)
    
    
    node = nuke.toNode('Write1') #Just for avoiding error. It will not use while running the code
    
    
    for i in nuke.selectedNodes():
        
        if i.Class()=='Write':
            shotname_list = i.knob('file').getValue()
            shotname = shotname_list.split('/')[-1]
            nodes =  ('"' +  shotname + '"  ' + '(' + i.name() + ')'  + '   -    '+'      Rendering.....')
            render_information.append(nodes)
            nuke.display('showChannels()', node, 'Render_Information')
            
            nuke.execute(i,1,10)
            
           
            render_information.pop(-1)
            nodes =  ('"' +  shotname + '"  ' + '(' + i.name() + ')'  + '   -    '+'      completed')
            render_information.append(nodes)
            nuke.display('showChannels()', node, 'Render_Information')

nuke.menu('Nodes').addMenu('RenderMultipleNodes',icon = 'Render.png').addCommand('Render selected Write nodes', RenderMultipleNodes, icon = 'ProjectionSolver.png')
