
from nwdiag import parser, builder, drawer


# sphinx extension
#.. seqdiag::
#
#    seqdiag admin {
#      A -> B -> C;
#    }


nw_diagram_definition = u"""
nwdiag {
  inet [shape = cloud];
  inet -- router;

  network {
    router;
    web01;
    web02;
  }

  network Sample_front {
    address = "192.168.10.0/24";

    // define group
    group web {
      web01 [address = ".1"];
      web02 [address = ".2"];
    }
  }
  network Sample_back {
    address = "192.168.20.0/24";
    web01 [address = ".1"];
    web02 [address = ".2"];
    db01 [address = ".101"];
    db02 [address = ".102"];

    // define network using defined nodes
    group db {
      db01;
      db02;
    }
  }

}
"""

nw_tree = parser.parse_string(nw_diagram_definition)
nw_diagram = builder.ScreenNodeBuilder.build(nw_tree)
nw_draw = drawer.DiagramDraw('PNG', nw_diagram, filename="nw_diagram.png")
nw_draw.draw()
nw_draw.save()
