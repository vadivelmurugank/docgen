
from packetdiag import parser, builder, drawer


# sphinx extension
#.. seqdiag::
#
#    seqdiag admin {
#      A -> B -> C;
#    }


packet_diagram_definition = u"""
packetdiag {
  colwidth = 32
  node_height = 72

  0-15: Source Port
  16-31: Destination Port
  32-63: Sequence Number
  64-95: Acknowledgment Number
  96-99: Data Offset
  100-105: Reserved
  106: URG [rotate = 270]
  107: ACK [rotate = 270]
  108: PSH [rotate = 270]
  109: RST [rotate = 270]
  110: SYN [rotate = 270]
  111: FIN [rotate = 270]
  112-127: Window
  128-143: Checksum
  144-159: Urgent Pointer
  160-191: (Options and Padding)
  192-223: data [colheight = 3]
   }
"""

packet_tree = parser.parse_string(packet_diagram_definition)
packet_diagram = builder.ScreenNodeBuilder.build(packet_tree)
packet_draw = drawer.DiagramDraw('PNG', packet_diagram, filename="packet_diagram.png")
packet_draw.draw()
packet_draw.save()
