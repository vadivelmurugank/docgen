
from actdiag import parser, builder, drawer


# sphinx extension
#.. seqdiag::
#
#    seqdiag admin {
#      A -> B -> C;
#    }


act_diagram_definition = u"""
actdiag {
  write -> convert -> image

  lane user {
     label = "User"
     write [label = "Writing reST"];
     image [label = "Get diagram IMAGE"];
  }
  lane actdiag {
     convert [label = "Convert reST to Image"];
  }

  A -> B -> C -> D;

  lane foo {
    A; B;
  }
  lane bar {
    C; D;
  }
   }
"""

act_tree = parser.parse_string(act_diagram_definition)
act_diagram = builder.ScreenNodeBuilder.build(act_tree)
act_draw = drawer.DiagramDraw('PNG', act_diagram, filename="act_diagram.png")
act_draw.draw()
act_draw.save()
