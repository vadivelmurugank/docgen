
from blockdiag import parser, builder, drawer


# sphinx extension
#.. seqdiag::
#
#    seqdiag admin {
#      A -> B -> C;
#    }


block_diagram_definition = u"""
   blockdiag {

    span_width = 200;
    span_height = 100;
    default_fontsize = 16;

    //orientation = portrait;
    default_linecolor = "blue";
    default_textcolor = "brown";
    //edge_layout = flowchart; 


    init -> runblock;
        runblock -> Card1;
        Card1 -> browser;
      Card1 -> Card2;
      Card2 -> Card1;
      browser <- Card1;
      browser  -> webserver;
      browser <- webserver;
      browser <- webserver;
      browser -> browser;
   }
"""

block_tree = parser.parse_string(block_diagram_definition)
block_diagram = builder.ScreenNodeBuilder.build(block_tree)
block_draw = drawer.DiagramDraw('PNG', block_diagram, filename="block_diagram.png")
block_draw.draw()
block_draw.save()
